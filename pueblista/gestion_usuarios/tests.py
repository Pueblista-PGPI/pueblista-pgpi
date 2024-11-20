from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from gestion_usuarios.forms import LoginForm
from gestion_usuarios.models import CustomUser
from django.utils.crypto import get_random_string

from gestion_usuarios.backends import DNIFechaNacimientoBackend

User = get_user_model()

class AuthenticationBackendTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            dni='12345678A',
            nombre='Test',
            apellidos='User',
            telefono='123456789',
            direccion_postal='Calle Falsa 123',
            fecha_nacimiento='2000-01-01',
            password=get_random_string(length=16),
        )

    def test_authenticate_valid_user(self):
        backend = DNIFechaNacimientoBackend()
        user = backend.authenticate(request=None,dni='12345678A', fecha_nacimiento='2000-01-01')
        self.assertIsNotNone(user)
        self.assertEqual(user.dni, '12345678A')

    def test_authenticate_invalid_user(self):
        backend = DNIFechaNacimientoBackend()
        user = backend.authenticate(request=None,dni='99999999A', fecha_nacimiento='1990-01-01')
        self.assertIsNone(user)
        
    def test_get_user_valid(self):
        user = DNIFechaNacimientoBackend().get_user(self.user.id)
        self.assertIsNotNone(user)
        self.assertEqual(user.dni, '12345678A')

    def test_get_user_invalid(self):
        non_existent_user_id = 9999
        user = DNIFechaNacimientoBackend().get_user(non_existent_user_id)
        self.assertIsNone(user)


class CustomUserModelTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            dni='87654321B',
            nombre='Jane',
            apellidos='Doe',
            telefono='987654321',
            direccion_postal='Calle Real 456',
            fecha_nacimiento='1995-01-01',
        )
        self.assertEqual(user.dni, '87654321B')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            dni='11223344C',
            nombre='Super',
            apellidos='User',
            telefono='123123123',
            direccion_postal='Calle Mayor 789',
            fecha_nacimiento='1980-01-01',
            password='superpassword'
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        
    def test_create_user_missing_dni(self):
        with self.assertRaisesMessage(ValueError, 'El DNI es obligatorio'):
            User.objects.create_user(
                dni=None,
                nombre='Jane',
                apellidos='Doe',
                telefono='987654321',
                direccion_postal='Calle Real 456',
                fecha_nacimiento='1995-01-01',
            )

    def test_create_user_missing_nombre(self):
        with self.assertRaisesMessage(ValueError, 'El nombre es obligatorio'):
            User.objects.create_user(
                dni='87654321B',
                nombre=None,
                apellidos='Doe',
                telefono='987654321',
                direccion_postal='Calle Real 456',
                fecha_nacimiento='1995-01-01',
            )

    def test_create_user_missing_apellidos(self):
        with self.assertRaisesMessage(ValueError, 'Los apellidos son obligatorios'):
            User.objects.create_user(
                dni='87654321B',
                nombre='Jane',
                apellidos=None,
                telefono='987654321',
                direccion_postal='Calle Real 456',
                fecha_nacimiento='1995-01-01',
            )

    def test_create_user_missing_telefono(self):
        with self.assertRaisesMessage(ValueError, 'El teléfono es obligatorio'):
            User.objects.create_user(
                dni='87654321B',
                nombre='Jane',
                apellidos='Doe',
                telefono=None,
                direccion_postal='Calle Real 456',
                fecha_nacimiento='1995-01-01',
            )

    def test_create_user_missing_direccion_postal(self):
        with self.assertRaisesMessage(ValueError, 'La dirección postal es obligatoria'):
            User.objects.create_user(
                dni='87654321B',
                nombre='Jane',
                apellidos='Doe',
                telefono='987654321',
                direccion_postal=None,
                fecha_nacimiento='1995-01-01',
            )

    def test_create_user_missing_fecha_nacimiento(self):
        with self.assertRaisesMessage(ValueError, 'La fecha de nacimiento es obligatoria'):
            User.objects.create_user(
                dni='87654321B',
                nombre='Jane',
                apellidos='Doe',
                telefono='987654321',
                direccion_postal='Calle Real 456',
                fecha_nacimiento=None,
            )


class LoginFormTests(TestCase):
    def test_login_form_valid(self):
        form_data = {'dni': '12345678A', 'fecha_nacimiento': '2000-01-01'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())



    def test_login_form_invalid_fecha_nacimiento(self):
        form_data = {'dni': '12345678A', 'fecha_nacimiento': 'invalid-date'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('fecha_nacimiento', form.errors)


class UserViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            dni='12345678A',
            nombre='Test',
            apellidos='User',
            telefono='123456789',
            direccion_postal='Calle Falsa 123',
            fecha_nacimiento='2000-01-01',
            password='testpassword'
        )
        self.admin_user = User.objects.create_superuser(
            dni='87654321B',
            nombre='Admin',
            apellidos='User',
            telefono='987654321',
            direccion_postal='Calle Verdadera 456',
            fecha_nacimiento='1980-01-01',
            password='adminpassword'
        )

    def test_login_view_valid_user(self):
        response = self.client.post(reverse('login'), {'dni': '12345678A', 'fecha_nacimiento': '2000-01-01'})
        self.assertRedirects(response, reverse('home'))  # Should redirect after login

    def test_login_view_invalid_user(self):
        response = self.client.post(reverse('login'), {'dni': 'invalid', 'fecha_nacimiento': '2000-01-01'})
        self.assertRedirects(response, reverse('login'))


    def test_logout_view(self):
        self.client.login(dni='12345678A', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_user_list_view_admin_access(self):
        self.client.login(dni='87654321B', password='adminpassword')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')

    def test_user_list_view_no_access(self):
        self.client.login(dni='12345678A', password='testpassword')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 403)  # Forbidden, since regular user should not access
        
    def test_perfil_view_authenticated_user(self):
        # Iniciar sesión con el usuario de prueba
        self.client.login(dni='12345678A', password='testpassword')
        # Solicitar la vista de perfil
        response = self.client.get(reverse('perfil'))
        # Verificar que la respuesta sea exitosa (código 200)
        self.assertEqual(response.status_code, 200)
        # Verificar que el contenido de la página contiene la información del usuario
        self.assertContains(response, 'Test User')
        self.assertContains(response, '12345678A')
        self.assertContains(response, 'Calle Falsa 123')
        self.assertContains(response, '123456789')

    def test_perfil_view_not_authenticated(self):
        # Solicitar la vista de perfil sin estar autenticado
        response = self.client.get(reverse('perfil'))
        # Verificar que la respuesta sea una redirección al login (código 302)
        self.assertEqual(response.status_code, 302)
        # Verificar que el usuario sea redirigido al login
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('perfil')}")


class DecoratorTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            dni='87654321B',
            nombre='Admin',
            apellidos='User',
            telefono='987654321',
            direccion_postal='Calle Verdadera 456',
            fecha_nacimiento='1980-01-01',
            password='adminpassword'
        )

    def test_tipo_usuario_requerido_superuser(self):
        self.client.login(dni='87654321B', password='adminpassword')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)  # Should allow superuser access

    def test_tipo_usuario_requerido_regular_user(self):
        user = User.objects.create_user(
            dni='11223344C',
            nombre='Regular',
            apellidos='User',
            telefono='111222333',
            direccion_postal='Calle Chica 789',
            fecha_nacimiento='1999-12-12',
            password='regularpassword'
        )
        self.client.login(dni='11223344C', password='regularpassword')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 403)  # Should forbid regular user


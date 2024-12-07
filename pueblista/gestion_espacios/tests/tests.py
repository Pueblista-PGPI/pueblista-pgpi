from django.test import TestCase
from gestion_espacios.models import EspacioPublico
from django.urls import reverse
from gestion_usuarios.models import CustomUser
from gestion_reservas.models import Reserva


class EspacioPublicoModelTests(TestCase):
    def setUp(self):
        self.espacio = EspacioPublico.objects.create(
            nombre='Parque Central',
            horario='08:00 - 20:00',
            descripcion='Un parque grande y bonito en el centro de la ciudad.',
            telefono='123456789',
            estado=EspacioPublico.DISPONIBLE
        )

    def test_create_espacio(self):
        espacio = EspacioPublico.objects.create(
            nombre='Biblioteca Municipal',
            horario='09:00 - 18:00',
            descripcion='Una biblioteca con una gran colección de libros.',
            telefono='987654321',
            estado=EspacioPublico.DISPONIBLE
        )
        self.assertEqual(espacio.nombre, 'Biblioteca Municipal')
        self.assertEqual(espacio.estado, EspacioPublico.DISPONIBLE)

    def test_editar_espacio(self):
        self.espacio.editar_espacio(
            nombre='Parque Renovado', estado=EspacioPublico.NO_DISPONIBLE, telefono='987654321'
        )
        self.assertEqual(self.espacio.nombre, 'Parque Renovado')
        self.assertEqual(self.espacio.estado, EspacioPublico.NO_DISPONIBLE)

    def test_editar_espacio_partial(self):
        self.espacio.editar_espacio(nombre='Parque Actualizado')
        self.assertEqual(self.espacio.nombre, 'Parque Actualizado')
        self.assertEqual(self.espacio.horario, '08:00 - 20:00')

    def test_editar_espacio_fotos(self):
        self.espacio.editar_espacio(fotos='path/to/photo.jpg')
        self.assertEqual(self.espacio.fotos, 'path/to/photo.jpg')

    def test_editar_espacio_telefono(self):
        self.espacio.editar_espacio(telefono='987654321')
        self.assertEqual(self.espacio.telefono, '987654321')

    def test_editar_espacio_horario(self):
        self.espacio.editar_espacio(horario='10:00 - 22:00')
        self.assertEqual(self.espacio.horario, '10:00 - 22:00')

    def test_editar_espacio_descripcion(self):
        self.espacio.editar_espacio(descripcion='Un parque renovado y moderno.')
        self.assertEqual(self.espacio.descripcion, 'Un parque renovado y moderno.')

    def test_editar_espacio_estado(self):
        self.espacio.editar_espacio(estado=EspacioPublico.NO_DISPONIBLE)
        self.assertEqual(self.espacio.estado, EspacioPublico.NO_DISPONIBLE)

    def test_borrar_espacio(self):
        espacio_id = self.espacio.id
        self.espacio.borrar_espacio()
        with self.assertRaises(EspacioPublico.DoesNotExist):
            EspacioPublico.objects.get(id=espacio_id)


class EspacioPublicoViewsTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            dni='12345678A',
            nombre='Admin',
            apellidos='User',
            telefono='123456789',
            direccion_postal='Calle Falsa 123',
            fecha_nacimiento='1990-01-01',
            password='admin',
            tipo_usuario=CustomUser.SUPERUSUARIO
        )
        self.client.login(username='12345678A', password='admin')
        self.espacio = EspacioPublico.objects.create(
            nombre='Parque Central',
            horario='08:00 - 20:00',
            descripcion='Un parque grande y bonito en el centro de la ciudad.',
            telefono='123456789',
            estado=EspacioPublico.DISPONIBLE
        )

    def test_list_view(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.espacio.nombre)

    def test_create_view(self):
        response = self.client.post(reverse('create'), {
            'nombre': 'Biblioteca Municipal',
            'horario': '09:00 - 18:00',
            'descripcion': 'Una biblioteca con una gran colección de libros.',
            'telefono': '987654321',
            'estado': EspacioPublico.DISPONIBLE
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            EspacioPublico.objects.filter(nombre='Biblioteca Municipal').exists()
        )

    def test_create_view_get(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')

    def test_edit_view(self):
        response = self.client.post(reverse('edit', args=[self.espacio.id]), {
            'nombre': 'Parque Renovado',
            'horario': '08:00 - 20:00',
            'descripcion': 'Un parque renovado en el centro de la ciudad.',
            'telefono': '123456789',
            'estado': EspacioPublico.NO_DISPONIBLE
        })
        self.assertEqual(response.status_code, 302)
        self.espacio.refresh_from_db()
        self.assertEqual(self.espacio.nombre, 'Parque Renovado')
        self.assertEqual(self.espacio.estado, EspacioPublico.NO_DISPONIBLE)

    def test_edit_view_get(self):
        response = self.client.get(reverse('edit', args=[self.espacio.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')

    def test_delete_view(self):
        response = self.client.post(reverse('delete', args=[self.espacio.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            EspacioPublico.objects.filter(id=self.espacio.id).exists()
        )

    def test_edit_view_post_with_fotos(self):
        with open('static/images/home/ayuntamiento.jpg', 'rb') as photo:
            response = self.client.post(reverse('edit', args=[self.espacio.id]), {
                'nombre': 'Parque Renovado',
                'horario': '08:00 - 20:00',
                'descripcion': 'Un parque renovado en el centro de la ciudad.',
                'telefono': '123456789',
                'estado': EspacioPublico.NO_DISPONIBLE,
                'fotos': photo,
                'espacio_especial': False,
                'limpieza': False
            })
        self.assertEqual(response.status_code, 302)
        self.espacio.refresh_from_db()
        self.assertEqual(str(self.espacio), 'Parque Renovado')
        self.assertEqual(self.espacio.estado, EspacioPublico.NO_DISPONIBLE)
        self.assertIsNotNone(self.espacio.fotos)

    def test_delete_view_get(self):
        response = self.client.get(reverse('delete', args=[self.espacio.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')

    def test_reservas_fecha_view_without_dates(self):
        reserva = Reserva.objects.create(
            espacio=self.espacio, fecha='2050-10-10', hora_inicio='10:00', hora_fin='12:00', usuario=self.user
        )
        reserva.save()
        
        response = self.client.get(
            reverse('reservas_fecha', args=[self.espacio.id]),
            {'date': '2050-10-10'},  # Enviar la fecha como parámetro GET.
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '10 de octubre de 2050')  # Verificar que la fecha aparece.


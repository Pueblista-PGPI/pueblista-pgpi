from django.test import TestCase, Client
from django.urls import reverse
from gestion_usuarios.models import CustomUser
from home.models import Configuracion

class HomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            dni='12345678A',
            password='12345',
            fecha_nacimiento='2000-01-01',
            nombre='Test',
            apellidos='User',
            telefono='123456789',
            direccion_postal='Calle Falsa 123'
        )
        self.client.login(dni='12345678A', password='12345')
        self.config = Configuracion.objects.create(id=1, texto_ayuntamiento="Texto inicial")

    def test_homepage_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pueblista")

    def test_contact_us(self):
        response = self.client.post(reverse('home'), {
            'message': 'This is a test message.'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Muchas gracias por tu ayuda.")

    def test_edit_information(self):
        response = self.client.post(reverse('home'), {
            'nuevo_ayuntamiento': 'Nuevo texto del ayuntamiento'
        })
        self.assertEqual(response.status_code, 302)  # Redirección después de guardar
        self.config.refresh_from_db()
        self.assertEqual(self.config.texto_ayuntamiento, 'Nuevo texto del ayuntamiento')
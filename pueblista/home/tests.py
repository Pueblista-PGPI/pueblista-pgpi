from unittest.mock import patch
from django.test import TestCase, Client
from django.urls import reverse
from gestion_usuarios.models import CustomUser
from home.models import AyuntamientoInfo
from gestion_notificaciones.models import Notificacion


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
            direccion_postal='Calle Falsa 123',
            tipo_usuario=CustomUser.SUPERUSUARIO
        )
        self.client.login(dni='12345678A', password='12345')

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

    def test_edit_ayuntamiento_info(self):
        info = AyuntamientoInfo.objects.create(
        titulo="Historia inicial",
        descripcion="Descripción inicial"
    )
        response = self.client.post(reverse('edit_ayuntamiento_info', args=[info.id]), {
        'titulo': 'Historia actualizada',
        'descripcion': 'Descripción actualizada'
         })
        self.assertEqual(response.status_code, 302)
        info.refresh_from_db()
        self.assertEqual(info.titulo, 'Historia actualizada')
        self.assertEqual(info.descripcion, 'Descripción actualizada')
    
    def test_edit_ayuntamiento_info_get(self):
        info = AyuntamientoInfo.objects.create(
        titulo="Historia inicial",
        descripcion="Descripción inicial"
        )
        response = self.client.get(reverse('edit_ayuntamiento_info', args=[info.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Historia inicial")
        
    def test_add_ayuntamiento_info(self):
        response = self.client.post(reverse('add_ayuntamiento_info'), {
        'titulo': 'Nueva historia',
        'descripcion': 'Nueva descripción'
        })
        self.assertEqual(response.status_code, 302)  
        info = AyuntamientoInfo.objects.last()
        self.assertEqual(info.titulo, 'Nueva historia')
        self.assertEqual(info.descripcion, 'Nueva descripción')
        
    def test_add_ayuntamiento_info_get(self):
        response = self.client.get(reverse('add_ayuntamiento_info'))
        self.assertEqual(response.status_code, 200)

    
    @patch('home.views.EmailBackend')
    def test_send_email_exception(self, mock_email_backend):    
        mock_email_backend.side_effect = Exception("Error en el envío de correo")
        response = self.client.post(reverse('home'), {
        'message': 'Mensaje que causará un error en el correo.'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ocurrió un error al enviar el mensaje')   

    def test_homepage_with_unread_notifications(self):
        Notificacion.objects.create(usuario=self.user, mensaje="Prueba", leida=False)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1')
 

    
    
class AyuntamientoInfoTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            dni='12345678A',
            password='12345',
            fecha_nacimiento='2000-01-01',
            nombre='Test',
            apellidos='User',
            telefono='123456789',
            direccion_postal='Calle Falsa 123',
            tipo_usuario=CustomUser.SUPERUSUARIO
        )
        self.client.login(dni='12345678A', password='12345')

    def test_create_ayuntamiento_info(self):
        info = AyuntamientoInfo.objects.create(
            titulo="Historia del pueblo",
            descripcion="Detalles históricos sobre el pueblo."
        )
        self.assertEqual(str(info), "Historia del pueblo")
        self.assertEqual(info.descripcion, "Detalles históricos sobre el pueblo.")

    def test_delete_ayuntamiento_info(self):
        info = AyuntamientoInfo.objects.create(
            titulo="Historia del pueblo",
            descripcion="Detalles históricos sobre el pueblo."
        )
        info.save()
        response = self.client.post(reverse('delete_ayuntamiento_info', args=[info.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(AyuntamientoInfo.objects.filter(id=info.id).exists())
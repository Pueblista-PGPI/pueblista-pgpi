from django.test import TestCase
from gestion_notificaciones.models import Notificacion
from django.urls import reverse
from gestion_usuarios.models import CustomUser


class NotificacionModelTests(TestCase):
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

    def test_create_notificacion(self):
        notificacion = Notificacion.objects.create(
            fecha='2021-01-01',
            mensaje='Nueva Notificacion',
            leida=False,
            usuario=self.user
        )
        self.assertEqual(notificacion.mensaje, 'Nueva Notificacion')

    def test_editar_notificacion(self):
        notificacion = Notificacion.objects.create(
            fecha='2021-01-01',
            mensaje='Nueva Notificacion',
            leida=False,
            usuario=self.user
        )
        
        notificacion.leida = True
        notificacion.mensaje = 'Notificacion Actualizada'
        notificacion.save()
        
        self.assertEqual(str(notificacion), 'Notificacion Actualizada')
        self.assertEqual(notificacion.leida, True)

    def test_borrar_notificacion(self):
        notificacion = Notificacion.objects.create(
            fecha='2021-01-01',
            mensaje='Nueva Notificacion',
            leida=False,
            usuario=self.user
        )
        
        notificacion_id = notificacion.id
        notificacion.delete()
        
        with self.assertRaises(Notificacion.DoesNotExist):
            Notificacion.objects.get(id=notificacion_id)
    
class NotificacionViewsTests(TestCase):
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
        self.notificacion = Notificacion.objects.create(
            fecha='2021-01-01',
            mensaje='Nueva Notificacion',
            leida=False,
            usuario=self.user
        )
    
    def test_mis_notificaciones(self):
        response = self.client.get(reverse('notificaciones'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nueva Notificacion')
    
    def test_marcar_leida(self):
        response = self.client.get(reverse('marcar_leida', kwargs={'notificacion_id': self.notificacion.id}))
        self.assertEqual(response.status_code, 302)
        self.notificacion.refresh_from_db()
        self.assertEqual(self.notificacion.leida, True)
    
    def test_borrar_notificacion(self):
        response = self.client.get(reverse('borrar_notificacion', kwargs={'notificacion_id': self.notificacion.id}))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Notificacion.DoesNotExist):
            Notificacion.objects.get(id=self.notificacion.id)
            
    def test_borrar_todas_leidas(self):
        self.notificacion.leida = True
        self.notificacion.save()
        
        response = self.client.get(reverse('borrar_todas_leidas'))
        self.assertEqual(response.status_code, 302)
        notificaciones = Notificacion.objects.filter(usuario=self.user)
        self.assertEqual(notificaciones.count(), 0)
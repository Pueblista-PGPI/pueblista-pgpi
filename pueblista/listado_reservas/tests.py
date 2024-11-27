from django.test import TestCase
from django.test import Client
from django.urls import reverse
from gestion_usuarios.models import CustomUser
from gestion_reservas.models import Reserva
from gestion_espacios.models import EspacioPublico
from gestion_reservas.models import Reserva
from datetime import datetime, time
from django.core.exceptions import ValidationError
from django.utils import timezone


class TestListadoReservas(TestCase):
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

        self.espacio = EspacioPublico.objects.create(
            nombre='Espacio de Prueba',
            horario='09:00-18:00',
            descripcion='Descripción del espacio de prueba',
            telefono='123456789'
        )
         # Crear una reserva de prueba
        self.reserva =  Reserva.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(17, 0),
            hora_fin=time(18, 0),
            estado=Reserva.REALIZADA
            
        )
        
    def test_listado_reservas(self):
        response = self.client.get(reverse('listado_reservas'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tus reservas")
        self.assertContains(response, "Espacio de Prueba")
        self.assertContains(response, "17:00")
        self.assertContains(response, "18:00")
        self.assertContains(response, "Realizada")

    def test_eliminar_reserva(self):
        response = self.client.post(reverse('eliminar_reserva', args=[self.reserva.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Reserva.objects.filter(id=self.reserva.id).exists())
        
    def test_modificar_estado(self):
        response = self.client.post(reverse('modificar_estado', args=[self.reserva.id]), 
            {
            "id_estado": Reserva.EN_CURSO
             }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Reserva.objects.get(id=self.reserva.id).estado, Reserva.EN_CURSO)
        
    def test_eliminar_reserva_no_existente(self):
        response = self.client.post(reverse('eliminar_reserva', args=[self.reserva.id + 1]), follow=True)
        self.assertEqual(response.status_code, 404)
    
    def test_modificar_estado_cancelada(self):
        response = self.client.post(reverse('modificar_estado', args=[self.reserva.id]), 
            {
            "id_estado": Reserva.CANCELADA
             }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Reserva.objects.filter(id=self.reserva.id).exists())
        
    def test_filtrar_fechas(self):
        response = self.client.get(reverse('listado_reservas'),{
            'fecha_inicio': self.reserva.fecha - timezone.timedelta(days=4),
            'fecha_fin': self.reserva.fecha + timezone.timedelta(days=4)
            }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tus reservas")
        self.assertContains(response, "Espacio de Prueba")
        self.assertContains(response, "17:00")
        self.assertContains(response, "18:00")
        self.assertContains(response, "Realizada")  

    
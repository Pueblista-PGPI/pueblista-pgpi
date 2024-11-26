from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Reserva
from gestion_espacios.models import EspacioPublico
from datetime import datetime, time
from gestion_usuarios.models import CustomUser
from django.urls import reverse
from gestion_reservas.models import SolicitudReservaEspecial

User = get_user_model()

class ReservaModelTests(TestCase):

    def setUp(self):
        # Crear un usuario de prueba
        self.user = CustomUser.objects.create_user(dni='12345678A', nombre='Test', apellidos='User', telefono='123456789', direccion_postal='Calle Falsa 123', fecha_nacimiento='2000-01-01')
        # Crear un espacio público de prueba
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

    def test_crear_reserva(self):
        # Crear una reserva
        reserva = Reserva.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            estado=Reserva.REALIZADA
        )
        self.assertEqual(reserva.usuario, self.user)
        self.assertEqual(reserva.espacio, self.espacio)
        self.assertEqual(reserva.estado, Reserva.REALIZADA)

    def test_reserva_estado_cancelada(self):
        # Crear una reserva con estado cancelado
        reserva = Reserva.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(10, 0),
            hora_fin=time(11, 0),
            estado=Reserva.CANCELADA
        )
        self.assertEqual(reserva.estado, Reserva.CANCELADA)

    def test_reserva_estado_en_curso(self):
        # Crear una reserva con estado en curso
        reserva = Reserva.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(11, 0),
            hora_fin=time(12, 0),
            estado=Reserva.EN_CURSO
        )
        self.assertEqual(reserva.estado, Reserva.EN_CURSO)

    def test_reserva_estado_finalizada(self):
        # Crear una reserva con estado finalizado
        reserva = Reserva.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(12, 0),
            hora_fin=time(13, 0),
            estado=Reserva.FINALIZADA
        )
        self.assertEqual(reserva.estado, Reserva.FINALIZADA)

    def test_reserva_horarios(self):
        # Crear una reserva y verificar los horarios
        reserva = Reserva.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(13, 0),
            hora_fin=time(14, 0),
            estado=Reserva.REALIZADA
        )
        self.assertEqual(reserva.hora_inicio, time(13, 0))
        self.assertEqual(reserva.hora_fin, time(14, 0))

    def test_crear_reserva_sin_fecha(self):
        # Intentar crear una reserva sin fecha
        with self.assertRaises(ValidationError):
            reserva = Reserva(
                usuario=self.user,
                espacio=self.espacio,
                hora_inicio=time(9, 0),
                hora_fin=time(10, 0),
                estado=Reserva.REALIZADA
            )
            reserva.full_clean()

    def test_crear_reserva_sin_hora_inicio(self):
        # Intentar crear una reserva sin hora de inicio
        with self.assertRaises(ValidationError):
            reserva = Reserva(
                usuario=self.user,
                espacio=self.espacio,
                fecha=datetime.now().date(),
                hora_fin=time(10, 0),
                estado=Reserva.REALIZADA
            )
            reserva.full_clean()

    def test_crear_reserva_sin_hora_fin(self):
        # Intentar crear una reserva sin hora de fin
        with self.assertRaises(ValidationError):
            reserva = Reserva(
                usuario=self.user,
                espacio=self.espacio,
                fecha=datetime.now().date(),
                hora_inicio=time(9, 0),
                estado=Reserva.REALIZADA
            )
            reserva.full_clean()

    def test_crear_reserva_sin_estado(self):
        # Intentar crear una reserva sin estado
        reserva = Reserva(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0)
        )
        self.assertEqual(reserva.estado, Reserva.REALIZADA)

    def test_crear_reserva_hora_inicio_mayor_hora_fin(self):
        # Intentar crear una reserva con hora de inicio mayor que la hora de fin
        with self.assertRaises(ValidationError):
            reserva = Reserva(
                usuario=self.user,
                espacio=self.espacio,
                fecha=datetime.now().date(),
                hora_inicio=time(10, 0),
                hora_fin=time(9, 0),
                estado=Reserva.REALIZADA
            )
            reserva.full_clean()

    def test_crear_reserva_fecha_pasada(self):
        # Intentar crear una reserva en una fecha pasada
        with self.assertRaises(ValidationError):
            reserva = Reserva(
                usuario=self.user,
                espacio=self.espacio,
                fecha=datetime(2000, 1, 1).date(),
                hora_inicio=time(9, 0),
                hora_fin=time(10, 0),
                estado=Reserva.REALIZADA
            )
            reserva.full_clean()

    def test_crear_reserva_espacio_no_disponible(self):
        # Intentar crear una reserva en un espacio no disponible
        self.espacio.estado = EspacioPublico.NO_DISPONIBLE
        self.espacio.save()
        with self.assertRaises(ValidationError):
            reserva = Reserva(
                usuario=self.user,
                espacio=self.espacio,
                fecha=datetime.now().date(),
                hora_inicio=time(9, 0),
                hora_fin=time(10, 0),
                estado=Reserva.REALIZADA
            )
            reserva.full_clean()
            
    def test_crear_reserva_espacio_y_horario_no_disponible(self):
        # Intentar crear una reserva en un espacio y horario no disponible

        reserva1 = Reserva(
            usuario=self.user,
            espacio=self.espacio,
            subespacio="No procede",
            fecha=datetime.now().date(),
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            estado=Reserva.REALIZADA
        )
        reserva1.save()
        with self.assertRaises(ValidationError):
            reserva2 = Reserva(
                usuario=self.user,
                espacio=self.espacio,
                subespacio="No procede",
                fecha=datetime.now().date(),
                hora_inicio=time(9, 0),
                hora_fin=time(10, 0),
                estado=Reserva.REALIZADA
            )
            reserva2.full_clean()
            
    def test_listar_reservas(self):
        # Listar todas las reservas
        reservas = Reserva.objects.all()
        self.assertEqual(reservas.count(), 1)
        self.assertEqual(reservas[0], self.reserva)
    
    def test_borrar_reserva(self):
        # Verificar que se puede borrar una reserva usando el método personalizado
        self.reserva.borrar_reserva()
        reservas = Reserva.objects.all()
        self.assertEqual(reservas.count(), 0)
    
    def test_modificar_reserva(self):
        # Modificar una reserva existente
        nueva_fecha = datetime.now().date()
        nueva_hora_inicio = time(15, 0)
        nueva_hora_fin = time(16, 0)
        nuevo_estado = Reserva.EN_CURSO
        nuevo_espacio = EspacioPublico.objects.create(
            nombre='Nuevo Espacio',
            horario='09:00-18:00',
            descripcion='Descripción del nuevo espacio',
            telefono='987654321'
        )

        self.reserva.modificar_reserva(
            fecha=nueva_fecha,
            hora_inicio=nueva_hora_inicio,
            hora_fin=nueva_hora_fin,
            estado=nuevo_estado,
            espacio=nuevo_espacio,
            subespacio="No procede",
            usuario=self.user
        )

        self.assertEqual(self.reserva.fecha, nueva_fecha)
        self.assertEqual(self.reserva.hora_inicio, nueva_hora_inicio)
        self.assertEqual(self.reserva.hora_fin, nueva_hora_fin)
        self.assertEqual(self.reserva.estado, nuevo_estado)
        self.assertEqual(self.reserva.espacio, nuevo_espacio)
        self.assertEqual(self.reserva.usuario, self.user)
        
class ReservaViewsTests(TestCase):
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
            nombre='Espacio de Prueba',
            horario='09:00-18:00',
            descripcion='Descripción del espacio de prueba',
            telefono='123456789',
            subespacios='Sala A, Sala B'
        )
        self.reserva = Reserva.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(17, 0),
            hora_fin=time(18, 0),
            estado=Reserva.REALIZADA
        )
    
    def test_acceso_a_calendario(self):
        # Verificar que se puede listar las reservas
        response = self.client.get(f'/espacios/{self.espacio.id}/reservas/')
        self.assertEqual(response.status_code, 200)

    def test_crear_reserva(self):
        # Verificar que se puede crear una reserva
        hora_inicio = time(9, 0)
        response = self.client.post(reverse('crear_reserva', args=[self.espacio.id]), {
            'usuario': self.user.id,
            'espacio': self.espacio.id,
            'fecha': datetime.now().date(),
            'hora_inicio': hora_inicio,
            'hora_fin': time(10, 0),
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Reserva.objects.filter(usuario=self.user, espacio=self.espacio, hora_inicio=hora_inicio).exists())

    def test_cancelar_reserva(self):
        # Verificar que se puede cancelar una reserva
        response = self.client.post(f'/espacios/{self.espacio.id}/reservas/cancelar/{self.reserva.id}/')
        self.assertEqual(response.status_code, 302)

        with self.assertRaises(Reserva.DoesNotExist):
            self.reserva.refresh_from_db()

        self.assertFalse(
            Reserva.objects.filter(
                usuario=self.user, espacio=self.espacio, hora_inicio=self.reserva.hora_inicio
            ).exists())

    def test_crear_reserva_sin_autenticacion(self):
        self.client.logout()  # Asegurarse de que el cliente no esté autenticado.
        response = self.client.post('/espacios/1/reservas/', {
            'usuario': self.user.id,
            'espacio': self.espacio.id,
            'hora_inicio': '10:00',
            'hora_fin': '11:00',
            'fecha': '2024-11-26'
        })
        self.assertEqual(response.status_code, 302)  # Verificar redirección.
        self.assertIn('/login/', response.url)

    def test_reserva_horas_invalidas(self):
        response = self.client.post(reverse('crear_reserva', args=[self.espacio.id]), {
            'fecha': datetime.now().date(),
            'hora_inicio': '14:00',
            'hora_fin': '13:00'
        }, follow=True)

        self.assertEqual(response.status_code, 200)  # La redirección debe completarse
        self.assertContains(response, "La hora de inicio debe ser menor a la hora de fin.")
        
    def test_reserva_espacio_inexistente(self):
        # Espacio no encontrado
        response = self.client.post(reverse('crear_reserva', args=[999]), {
            'fecha': datetime.now().date(),
            'hora_inicio': '10:00',
            'hora_fin': '11:00'
        }, follow=True)

        self.assertEqual(response.status_code, 404) 

    def test_cancelar_reserva_inexistente(self):
        # Reserva no encontrada
        response = self.client.post(f'/espacios/{self.espacio.id}/reservas/cancelar/999/')
        self.assertEqual(response.status_code, 404)
    
    def test_reserva_fecha_pasada(self):
        response = self.client.post(reverse('crear_reserva', args=[self.espacio.id]), {
            'fecha': '2020-11-26',
            'hora_inicio': '10:00',
            'hora_fin': '11:00'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No se pueden hacer reservas en fechas pasadas.")
        
    def test_crear_solicitud_reserva_especial(self):
        session = self.client.session
        session['fecha'] = str(datetime.now().date())
        session.save()
        response = self.client.post(reverse('solicitud_reserva_especial', args=[self.espacio.id]), {
            'usuario': self.user.id,
            'espacio': self.espacio.id,
            'fecha': datetime.now().date(),
            'hora_inicio': time(9, 0),
            'hora_fin': time(10, 0),
            'motivo': 'Test motivo',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(SolicitudReservaEspecial.objects.filter(usuario=self.user, espacio=self.espacio).exists())


    def test_aceptar_solicitud_crea_reserva(self):
        # Realizar la solicitud de aceptación pasando el id correcto
        solicitud = SolicitudReservaEspecial.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            motivo='Test motivo'
        )
        solicitud.save()       
        
        response = self.client.post(reverse('aceptar_solicitud', kwargs={'id': self.espacio.id}), {
            'solicitud_id': solicitud.id,
            'nombre_reserva': 'Reserva de prueba'
        }, follow=True)

        # Verificar que la respuesta es correcta
        self.assertEqual(response.status_code, 200)
        
        # Verificar que la solicitud fue aceptada y ya no está en la base de datos
        self.assertTrue(SolicitudReservaEspecial.objects.filter(id=solicitud.id, estado='ACEPTADA').exists())

        # Verificar que la reserva fue creada
        self.assertTrue(Reserva.objects.filter(usuario=self.user, espacio=self.espacio).exists())

    def test_aceptar_solicitud_cancelar_reservas_conflictivas(self):
        # Crear una reserva conflictiva para verificar que se cancelan correctamente
        solicitud = SolicitudReservaEspecial.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            motivo='Test motivo'
        )
        solicitud.save()    
        
        conflictiva = Reserva.objects.create(
            fecha=solicitud.fecha,
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            nombre='Reserva conflictiva',
            estado=Reserva.REALIZADA,
            espacio=self.espacio,
            usuario=self.user
        )
        conflictiva.save()
        
        self.assertRaises(ValidationError, self.client.post, reverse('aceptar_solicitud', kwargs={'id': self.espacio.id}), {
            'solicitud_id': solicitud.id,
            'nombre_reserva': 'Reserva de prueba'
        }, follow=True)

    def test_aceptar_solicitud_con_limpieza_crea_reservas_de_limpieza(self):
        # Crear una solicitud de reserva especial con limpieza
        self.espacio.limpieza = True
        self.espacio.save()
        
        solicitud = SolicitudReservaEspecial.objects.create(
        usuario=self.user,
        espacio=self.espacio,
        fecha=datetime.now().date() + timezone.timedelta(days=4),
        hora_inicio=time(9, 0),
        hora_fin=time(10, 0),
        motivo='Test motivo'
        )
        solicitud.save()    
        

        # Realizar la solicitud de aceptación
        response = self.client.post(reverse('aceptar_solicitud', kwargs={'id': self.espacio.id}), {
            'solicitud_id': solicitud.id,
            'nombre_reserva': 'Reserva de prueba'
        }, follow=True)

        # Verificar que se crean las reservas de limpieza para los días previos y posteriores
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Reserva.objects.filter(nombre='LIMPIEZA', espacio=self.espacio).count(), 2)

    def test_cancelar_reservas_por_reserva_especial(self):
        # Crear una reserva conflictiva para verificar que se cancelan correctamente
        general = EspacioPublico.objects.create(
            nombre='Salón Sociocultural de Reuniones',
            horario='09:00-18:00',
            descripcion='Descripción del espacio conflictivo',
            telefono='999999999'
        )
        general.save()
        conflictivo = EspacioPublico.objects.create(
            nombre='Sala Guadalinfo',
            horario='09:00-18:00',
            descripcion='Descripción del espacio conflictivo',
            telefono='999999999'
        )
        conflictivo.save()
        solicitud = SolicitudReservaEspecial.objects.create(
            usuario=self.user,
            espacio=general,
            fecha=datetime.now().date(),
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            motivo='Test motivo'
        )
        solicitud.save()    
        
        conflictiva = Reserva.objects.create(
            fecha=solicitud.fecha,
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            nombre='Reserva conflictiva',
            estado=Reserva.REALIZADA,
            espacio=conflictivo,
            usuario=self.user
        )
        conflictiva.save()
        
        response = self.client.post(reverse('aceptar_solicitud', kwargs={'id': general.id}), {
            'solicitud_id': solicitud.id,
            'nombre_reserva': 'Reserva de prueba'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(Reserva.objects.filter(nombre='Reserva conflictiva', espacio=conflictivo).exists())
    
    def test_cancelar_solicitudes_pendientes(self):
        # Crear una solicitud pendiente para verificar que se cancela correctamente
        solicitud = SolicitudReservaEspecial.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            motivo='Test motivo',
            estado='Pendiente'
        )
        solicitud.save()    
        
        response = self.client.post(reverse('solicitudes_pendientes', kwargs={'id': self.espacio.id}),{
            'solicitud_id': solicitud.id,
            'motivo':'Se te cancela la solicitud'
            }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(SolicitudReservaEspecial.objects.filter(id=solicitud.id, estado='Cancelada').exists())
        
    def test_crear_reserva_salones_biblioteca_fallida(self):
        self.espacio.nombre = 'Salón Sociocultural de Reuniones'
        self.espacio.save()
        
        espacio_conflictivo = EspacioPublico.objects.create(
            nombre='Sala Guadalinfo',
            horario='09:00-18:00',
            descripcion='Descripción del espacio conflictivo',
            telefono='999999999'
        )
        espacio_conflictivo.save()
        
        response = self.client.post(reverse('crear_reserva', args=[espacio_conflictivo.id]), {
            'usuario' : self.user,
            'espacio' : espacio_conflictivo,
            'fecha' : datetime.now().date(),
            'hora_inicio' : time(17, 0),
            'hora_fin' : time(18, 0),
            'estado' : Reserva.REALIZADA
        }, follow=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ya existe una reserva en el Salón de Reuniones en este intervalo.")
        
    def test_obtener_solicitud_reserva_especial(self):
        solicitud = SolicitudReservaEspecial.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            motivo='Test motivo'
        )
        solicitud.save()
        
        response = self.client.get(reverse('solicitud_reserva_especial', args=[self.espacio.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.espacio.nombre)
    
    ## Copilot
    
    def test_solicitud_reserva_especial_mensaje_error(self):
        session = self.client.session
        session['fecha'] = str(datetime.now().date())
        session.save()
        SolicitudReservaEspecial.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            motivo='Test motivo',
            estado='PENDIENTE'
        )
        response = self.client.post(reverse('solicitud_reserva_especial', args=[self.espacio.id]), {
            'usuario': self.user.id,
            'espacio': self.espacio.id,
            'fecha': datetime.now().date(),
            'hora_inicio': time(9, 0),
            'hora_fin': time(10, 0),
            'motivo': 'Test motivo',
        }, follow=True)
        self.assertContains(response, 'Ya has solicitado una reserva especial para este espacio en esta fecha.')

    def test_aceptar_solicitud_crea_reserva(self):
        solicitud = SolicitudReservaEspecial.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date(),
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            motivo='Test motivo'
        )
        response = self.client.post(reverse('aceptar_solicitud', kwargs={'id': self.espacio.id}), {
            'solicitud_id': solicitud.id,
            'nombre_reserva': 'Reserva de prueba'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Reserva.objects.filter(usuario=self.user, espacio=self.espacio).exists())

    def test_aceptar_solicitud_crea_reservas_limpieza(self):
        self.espacio.limpieza = True
        self.espacio.save()
        solicitud = SolicitudReservaEspecial.objects.create(
            usuario=self.user,
            espacio=self.espacio,
            fecha=datetime.now().date() + timezone.timedelta(days=4),
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            motivo='Test motivo'
        )
        response = self.client.post(reverse('aceptar_solicitud', kwargs={'id': self.espacio.id}), {
            'solicitud_id': solicitud.id,
            'nombre_reserva': 'Reserva de prueba'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Reserva.objects.filter(nombre='LIMPIEZA', espacio=self.espacio).count(), 2)

    def test_cancelar_reservas_por_reserva_especial(self):
        general = EspacioPublico.objects.create(
            nombre='Salón Sociocultural de Reuniones',
            horario='09:00-18:00',
            descripcion='Descripción del espacio conflictivo',
            telefono='999999999'
        )
        conflictivo = EspacioPublico.objects.create(
            nombre='Sala Guadalinfo',
            horario='09:00-18:00',
            descripcion='Descripción del espacio conflictivo',
            telefono='999999999'
        )
        solicitud = SolicitudReservaEspecial.objects.create(
            usuario=self.user,
            espacio=general,
            fecha=datetime.now().date(),
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            motivo='Test motivo'
        )
        Reserva.objects.create(
            fecha=solicitud.fecha,
            hora_inicio=time(9, 0),
            hora_fin=time(10, 0),
            nombre='Reserva conflictiva',
            estado=Reserva.REALIZADA,
            espacio=conflictivo,
            usuario=self.user
        )
        response = self.client.post(reverse('aceptar_solicitud', kwargs={'id': general.id}), {
            'solicitud_id': solicitud.id,
            'nombre_reserva': 'Reserva de prueba'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Reserva.objects.filter(nombre='Reserva conflictiva', espacio=conflictivo).exists())

    def test_crear_reserva_fecha_pasada(self):
        response = self.client.post(reverse('crear_reserva', args=[self.espacio.id]), {
            'fecha': '2020-11-26',
            'hora_inicio': '10:00',
            'hora_fin': '11:00'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No se pueden hacer reservas en fechas pasadas.")

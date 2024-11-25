from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Reserva
from gestion_espacios.models import EspacioPublico
from datetime import datetime, time

User = get_user_model()

class ReservaModelTests(TestCase):

    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(dni='12345678A', nombre='Test', apellidos='User', telefono='123456789', direccion_postal='Calle Falsa 123', fecha_nacimiento='2000-01-01')
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
            usuario=self.user
        )

        self.assertEqual(self.reserva.fecha, nueva_fecha)
        self.assertEqual(self.reserva.hora_inicio, nueva_hora_inicio)
        self.assertEqual(self.reserva.hora_fin, nueva_hora_fin)
        self.assertEqual(self.reserva.estado, nuevo_estado)
        self.assertEqual(self.reserva.espacio, nuevo_espacio)
        self.assertEqual(self.reserva.usuario, self.user)
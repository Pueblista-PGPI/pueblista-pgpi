# pragma: no cover
from locust import HttpUser, task, between
from datetime import datetime
import random  # Para seleccionar un espacio aleatorio si lo prefieres
from io import BytesIO  # Para simular subida de archivo

# Clase 1: GestionUsuarios
class GestionUsuariosLoadTest(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        """Autentica al usuario y guarda las cookies de sesión de forma automática."""
        response = self.client.post(
            "/auth/login/",
            data={
                "dni": '11111111A',
                "fecha_nacimiento": '2000-01-01',
            },
            allow_redirects=True,
        )
        if response.status_code == 200 and "csrftoken" in response.cookies:
            self.csrf_token = response.cookies["csrftoken"]
        else:
            print(f"Error en inicio de sesión para 11111111A: {response.status_code}, {response.text}")
            self.environment.runner.quit()  # Detener si no se puede hacer login

    @task(1)
    def user_list(self):
        """Accede a la lista de usuarios con las cookies de sesión gestionadas automáticamente."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/auth/user_list/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al acceder a /auth/user_list/: {response.status_code}")

    @task(2)
    def perfil(self):
        """Accede al perfil de cada usuario con las cookies de sesión gestionadas automáticamente."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/auth/perfil/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al acceder a /auth/perfil/: {response.status_code}")

    @task(2)
    def logout(self):
        """Cierra la sesión de cada usuario con las cookies de sesión gestionadas automáticamente."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/auth/logout/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al acceder a /auth/logout/: {response.status_code}")



# Clase 2: GestionReservas
class GestionReservasLoadTest(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        """Autentica al usuario y guarda las cookies de sesión de forma automática."""
        response = self.client.post(
            "/auth/login/",  # Ruta de login según las URLs generales
            data={
                "dni": '11111111A',
                "fecha_nacimiento": '2000-01-01',
            },
            allow_redirects=True,
        )
        if response.status_code == 200 and "csrftoken" in response.cookies:
            self.csrf_token = response.cookies["csrftoken"]
        else:
            print(f"Error en inicio de sesión para 11111111A: {response.status_code}, {response.text}")
            self.environment.runner.quit()  # Detener si no se puede hacer login
    
    @task(2)
    def obtener_espacios(self):
        """Obtiene los espacios disponibles de la base de datos."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/espacios/list/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al obtener los espacios: {response.status_code}")


    @task(1)
    def mis_reservas(self):
        """Accede a las reservas del usuario autenticado."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/mis_reservas/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al obtener las reservas del usuario: {response.status_code}")

    @task(1)
    def espacio_reservas(self):
        """Consulta las reservas de un espacio específico."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get(f"/espacios/21/reservas/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al obtener las reservas del espacio: {response.status_code}")


    @task(1)
    def solicitudes_pendientes(self):
        """Consulta las solicitudes de reserva pendientes."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/espacios/18/reservas/solicitudes-pendientes", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al obtener las solicitudes pendientes: {response.status_code}")
                
from locust import HttpUser, task, between
from datetime import datetime


# Clase 1: GestionUsuarios
class GestionUsuariosLoadTest(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        """Autentica al usuario y guarda las cookies de sesión de forma automática."""
        response = self.client.post(
            "/auth/login/",
            data={
                "dni": '11111111A',
                "fecha_nacimiento": '2000-01-01',
            },
            allow_redirects=True,
        )
        if response.status_code == 200 and "csrftoken" in response.cookies:
            self.csrf_token = response.cookies["csrftoken"]
        else:
            print(f"Error en inicio de sesión para 11111111A: {response.status_code}, {response.text}")
            self.environment.runner.quit()  # Detener si no se puede hacer login

    @task(1)
    def user_list(self):
        """Accede a la lista de usuarios con las cookies de sesión gestionadas automáticamente."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/auth/user_list/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al acceder a /auth/user_list/: {response.status_code}")

    @task(2)
    def perfil(self):
        """Accede al perfil de cada usuario con las cookies de sesión gestionadas automáticamente."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/auth/perfil/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al acceder a /auth/perfil/: {response.status_code}")

    @task(2)
    def logout(self):
        """Cierra la sesión de cada usuario con las cookies de sesión gestionadas automáticamente."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/auth/logout/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al acceder a /auth/logout/: {response.status_code}")


# Clase 2: GestionReservas
class GestionReservasLoadTest(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        """Autentica al usuario y guarda las cookies de sesión de forma automática."""
        response = self.client.post(
            "/auth/login/",  # Ruta de login según las URLs generales
            data={
                "dni": '11111111A',
                "fecha_nacimiento": '2000-01-01',
            },
            allow_redirects=True,
        )
        if response.status_code == 200 and "csrftoken" in response.cookies:
            self.csrf_token = response.cookies["csrftoken"]
        else:
            print(f"Error en inicio de sesión para 11111111A: {response.status_code}, {response.text}")
            self.environment.runner.quit()  # Detener si no se puede hacer login
    
    @task(2)
    def crear_reserva(self):
        """Crea una nueva reserva."""
        headers = {"X-CSRFToken": self.csrf_token, "Referer": "https://pueblista-pgpi.onrender.com/espacios/21/reservas/crear/"}  # Incluir el token CSRF
        with self.client.post(
            "/espacios/21/reservas/crear/",
            data={
                "fecha": datetime.now().strftime("%Y-%m-%d"),
                "hora_inicio": "09:00",
                "hora_fin": "10:00",
            },
            cookies=self.client.cookies,
            headers=headers,
            catch_response=True,
            allow_redirects=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al crear la reserva: {response.status_code}")

    @task(1)
    def mis_reservas(self):
        """Accede a las reservas del usuario autenticado."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/mis_reservas/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al obtener las reservas del usuario: {response.status_code}")

    @task(1)
    def espacio_reservas(self):
        """Consulta las reservas de un espacio específico."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get(f"/espacios/21/reservas/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al obtener las reservas del espacio: {response.status_code}")

    @task(1)
    def solicitudes_pendientes(self):
        """Consulta las solicitudes de reserva pendientes."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/espacios/18/reservas/solicitudes-pendientes", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al obtener las solicitudes pendientes: {response.status_code}")


#from locust import HttpUser, task, between
class GestionEspaciosLoadTest(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        """Autentica al usuario y guarda las cookies de sesión de forma automática."""
        response = self.client.post(
            "/auth/login/",  # Ruta para login
            data={"dni": "11111111A", "fecha_nacimiento": "2000-01-01"},
            allow_redirects=True
        )
        
        # Verificar respuesta de login
        if response.status_code == 200:
            # Verificar si las cookies contienen el csrftoken
            if "csrftoken" in response.cookies:
                self.csrf_token = response.cookies["csrftoken"]
                print("CSRF Token encontrado:", self.csrf_token)
            else:
                print("CSRF Token no encontrado en las cookies")
                self.environment.runner.quit()  # Detener si no se puede obtener el CSRF
        else:
            print(f"Error al hacer login: {response.status_code}, {response.text}")
            self.environment.runner.quit()  # Detener si no se puede hacer login

    @task(1)
    def create_space(self):
        """Crea un nuevo espacio"""
        # Verifica si el CSRF Token está presente
        if not hasattr(self, 'csrf_token'):
            print("CSRF Token no disponible")
            return

        data = {
            "nombre": "Nuevo espacio de prueba",
            "horario": "9:00 - 18:00",
            "descripcion": "Este es un espacio de prueba",
            "telefono": "912345678",
            "estado": "activo",
            "subespacios": "Sala A, Sala B",
            "espacio_especial": False,
            "limpieza": False,
        }

        # Revisar cookies y headers antes de la petición
        print(f"Cookies antes de la solicitud: {self.client.cookies}")
        print(f"CSRF Token en el header: {self.csrf_token}")

        headers = {
        "X-CSRFToken": self.csrf_token,
        "Referer": "https://pueblista-pgpi.onrender.com/espacios/create/"
        }
        with self.client.post(
            "/espacios/create/",
            data=data,
            cookies=self.client.cookies,
            headers=headers,
            catch_response=True,
            allow_redirects=True
        ) as response:
            if response.status_code == 200:
                print("Espacio creado con éxito.")
                response.success()
            else:
                print(f"Error al crear el espacio: {response.status_code}, {response.text}")
                response.failure(f"Error al crear el espacio: {response.status_code}")

    @task(2)
    def reservas_fecha(self):
        """Obtiene las reservas de un espacio por fecha"""
        with self.client.get(
            "/espacios/reservas_fecha/21/",  # Ruta del espacio
            cookies=self.client.cookies,  # Usamos las cookies gestionadas automáticamente
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al obtener las reservas por fecha: {response.status_code}")

    @task(2)
    def obtener_espacios(self):
        """Obtiene los espacios disponibles de la base de datos."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/espacios/list/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al obtener los espacios: {response.status_code}")
                
class GestionHomePageLoadTest(HttpUser):

    def on_start(self):
        """Autentica al usuario y guarda las cookies de sesión de forma automática."""
        response = self.client.post(
            "/auth/login/",  # Ruta para login
            data={"dni": "11111111A", "fecha_nacimiento": "2000-01-01"},
            allow_redirects=True
        )
        
        # Verificar respuesta de login
        if response.status_code == 200:
            # Verificar si las cookies contienen el csrftoken
            if "csrftoken" in response.cookies:
                self.csrf_token = response.cookies["csrftoken"]
                print("CSRF Token encontrado:", self.csrf_token)
            else:
                print("CSRF Token no encontrado en las cookies")
                self.environment.runner.quit()  # Detener si no se puede obtener el CSRF
        else:
            print(f"Error al hacer login: {response.status_code}, {response.text}")
            self.environment.runner.quit()  # Detener si no se puede hacer login
    
    @task(1)
    def test_obtener_homepage(self):
        """Obtiene la página de inicio."""
        headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
        with self.client.get("/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al obtener la página de inicio: {response.status_code}")

    @task(1)
    def test_enviar_correo(self):
        """Envía un correo de prueba."""
        headers = {
            "X-CSRFToken": self.csrf_token,
            "Referer": "https://pueblista-pgpi.onrender.com/" 
        }
        with self.client.post(
            "/",
            data={
                "message": "Este es un mensaje de prueba"
            },
            cookies=self.client.cookies,
            headers=headers,
            catch_response=True,
            allow_redirects=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error al enviar el correo: {response.status_code}")
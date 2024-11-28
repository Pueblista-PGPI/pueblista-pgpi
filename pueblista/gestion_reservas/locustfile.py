from locust import HttpUser, task, between
from datetime import datetime
import random  # Para seleccionar un espacio aleatorio si lo prefieres

class GestionUsuariosLoadTest(HttpUser):
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
            print(f"Status Code: {response.status_code}")  # Para ver el código de estado
            print(f"Content-Type: {response.headers.get('Content-Type')}")  # Para ver el tipo de contenido
            
            if response.status_code == 200:
                # Verifica que el contenido sea JSON
                if 'application/json' in response.headers.get('Content-Type', ''):
                    try:
                        espacios = response.json()  # Suponiendo que la respuesta es una lista de espacios
                        if espacios:
                            self.espacio_id = random.choice(espacios)["id"]  # Seleccionamos un espacio aleatorio
                            response.success()
                        else:
                            response.failure("No se encontraron espacios disponibles.")
                    except ValueError:
                        response.failure(f"Error al analizar la respuesta JSON: {response.text}")
                else:
                    response.failure(f"El contenido no es JSON: {response.headers.get('Content-Type')}")
            else:
                response.failure(f"Error al obtener espacios: {response.status_code}")


    @task(1)
    def crear_reserva(self):
        """Crea una nueva reserva usando el espacio obtenido dinámicamente."""
        if hasattr(self, 'espacio_id'):
            headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
            today = datetime.today().strftime('%Y-%m-%d')  # Fecha de hoy
            data = {
                "fecha": today,  # Usamos la fecha actual
                "hora_inicio": "10:00:00",
                "hora_fin": "12:00:00",
                "espacio": self.espacio_id,  # Usamos el ID del espacio obtenido
                "subespacio": "Sala A",  # Subespacio, si aplica
            }
            with self.client.post("/espacios/1/reservas/crear/", cookies=self.client.cookies, headers=headers, data=data, catch_response=True) as response:
                if response.status_code == 200:
                    # Suponiendo que el ID de la reserva esté en la respuesta
                    self.reserva_id = response.json().get("id")  # Guarda el ID de la reserva
                    response.success()
                else:
                    response.failure(f"Error al crear la reserva: {response.status_code}")
        else:
            print("No se ha obtenido un espacio, no se puede crear la reserva.")

    @task(1)
    def cancelar_reserva(self):
        """Cancela la reserva que se ha creado anteriormente."""
        if hasattr(self, 'reserva_id'):
            headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
            with self.client.post(f"/espacios/1/reservas/cancelar/{self.reserva_id}/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Error al cancelar la reserva: {response.status_code}")
        else:
            print("No se ha creado una reserva, no se puede cancelar.")

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
        if hasattr(self, 'espacio_id'):
            headers = {"X-CSRFToken": self.csrf_token}  # Incluir el token CSRF
            with self.client.get(f"/espacios/{self.espacio_id}/reservas/", cookies=self.client.cookies, headers=headers, catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Error al obtener las reservas del espacio: {response.status_code}")
        else:
            print("No se ha obtenido un espacio, no se pueden consultar las reservas.")

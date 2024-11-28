from locust import HttpUser, task, between

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

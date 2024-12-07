from django.test import TestCase
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.selenium.common import launch_chrome

class GestionUsuariosSeleniumTests(TestCase):
    """
    Pruebas funcionales de Selenium para el módulo gestion_usuarios.
    """
    @classmethod
    def setUpClass(cls):
        """
        Configura el entorno de Selenium antes de todas las pruebas.
        """
        super().setUpClass()
        # Inicia el driver de Chrome
        cls.driver = launch_chrome()
        cls.base_url = "http://127.0.0.1:8000/auth/login/"

    @classmethod
    def tearDownClass(cls):
        """
        Cierra el navegador después de todas las pruebas.
        """
        if cls.driver:
            cls.driver.quit()
        super().tearDownClass()
           
    
    def test_login_and_logout(self):
        """
        Prueba el inicio de sesión y cierre de sesión en la aplicación.
        """

        driver = self.driver
        driver.set_window_size(1004, 1124)  # Establecer tamaño de ventana

        try:
            # Abre la página de login
            driver.get("http://localhost:8000/auth/login/?next=/")

            # Ingresar el DNI
            dni_field = driver.find_element(By.ID, "id_dni")
            dni_field.click()
            dni_field.send_keys("11111111A")

            # Ingresar la fecha de nacimiento
            birth_date_field = driver.find_element(By.ID, "id_fecha_nacimiento")
            birth_date_field.click()
            birth_date_field.send_keys("01-01-2000")

            # Hacer clic en el botón "Iniciar sesión"
            submit_button = driver.find_element(By.CSS_SELECTOR, ".d-block")
            submit_button.click()

            # Esperar hasta que la página de inicio esté cargada (esperar la presencia del elemento logout)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Cerrar sesión"))
            )

            # Hacer clic en el enlace "Cerrar sesión"
            logout_link = driver.find_element(By.LINK_TEXT, "Cerrar sesión")
            logout_link.click()

            # Pausa para observar el cierre de sesión
            time.sleep(3)

        except Exception as e:
            self.fail(f"Error durante la prueba: {e}")
    
    def test_eliminar_datos_usuario(self):
        driver = self.driver

        try:
            # Carga la página de inicio de sesión
            driver.get("http://localhost:8000/auth/login/?next=/")

            # Ingresar DNI
            driver.find_element(By.ID, "id_dni").send_keys("11111111A")

            # Ingresar fecha de nacimiento
            birth_date = driver.find_element(By.ID, "id_fecha_nacimiento")
            birth_date.send_keys("01-01-2000")
            birth_date.send_keys(Keys.ENTER)

            # Iniciar sesión
            driver.find_element(By.CSS_SELECTOR, ".d-block").click()

            # Navegar al perfil del usuario
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Perfil"))
            ).click()

            # Hacer clic en "Eliminar mis datos"
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn > strong"))
            ).click()

            # Esperar a que el modal sea visible
            modal = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "confirmModal"))
            )

            # Confirmar la eliminación
            confirm_delete_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "confirmDelete"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", confirm_delete_button)
            confirm_delete_button.click()

            # Validar que el modal se cerró
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element((By.ID, "confirmModal"))
            )

            # Validar redirección
            WebDriverWait(driver, 10).until(
                EC.url_contains("auth/login")
            )
            print("Eliminación completada y sesión cerrada exitosamente.")

        except Exception as e:
            driver.save_screenshot("error_screenshot.png")  # Captura para depuración
            self.fail(f"Error durante la prueba: {e}")
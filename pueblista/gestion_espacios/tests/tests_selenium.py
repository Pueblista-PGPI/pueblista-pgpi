from django.test import TestCase
import time
import tempfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.selenium.common import launch_chrome

class GestionEspaciosSeleniumTests(TestCase):
    """
    Pruebas funcionales de Selenium para el módulo gestion_espacios.
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
    
    def test_crear_espacio(self):
        """
        Prueba la creación de un espacio.
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
            
            # Navegar a la sección "Espacios".
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Espacios"))
            ).click()

            driver.find_element(By.LINK_TEXT, "Crear Nuevo Espacio").click()

            # Completar el formulario para crear un espacio.
            driver.find_element(By.ID, "id_nombre").send_keys("Espacio de prueba")
            driver.find_element(By.ID, "id_horario").send_keys("Todos los días de 9:00 a 14:00")
            driver.find_element(By.ID, "id_descripcion").send_keys("Descripción de prueba")
            driver.find_element(By.ID, "id_telefono").send_keys("666666666")

            # Subir una imagen (simulada).
            with tempfile.NamedTemporaryFile(suffix=".jpeg") as temp_file:
                temp_file.write(b"Fake image content")  # Contenido simulado
                temp_file.flush()  # Asegura que el contenido se escribe al disco
                driver.find_element(By.ID, "id_fotos").send_keys(temp_file.name)
            
            # Seleccionar opciones adicionales.
            try:
                # Encuentra el checkbox
                espacio_especial_checkbox = driver.find_element(By.ID, "id_espacio_especial")

                # Desplázate al checkbox
                driver.execute_script("arguments[0].click;", espacio_especial_checkbox)

            except Exception as e:
                 # Captura pantalla para depuración
                driver.save_screenshot("error_click_checkbox.png")
                self.fail(f"Error al intentar hacer clic en el checkbox: {e}")

           
                driver.find_element(By.ID, "id_limpieza").click()

                # Guardar el espacio.
                driver.find_element(By.CSS_SELECTOR, ".btn > strong").click()

                # Validar resultado esperado
                WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "selector_del_mensaje_exitoso"), "Espacio creado exitosamente")
                )
        
        except Exception as e:
            driver.save_screenshot("error_screenshot.png")  # Captura para depuración
            self.fail(f"Error durante la prueba: {e}")    
    
    def test_eliminar_espacio(self):
        """
        Prueba la eliminación de un espacio.
        """
        driver = self.driver
        driver.set_window_size(1004, 1124)

        try:
            # Iniciar sesión
            driver.get(self.base_url)
            driver.find_element(By.ID, "id_dni").send_keys("11111111A")
            driver.find_element(By.ID, "id_fecha_nacimiento").send_keys("01-01-2000")
            driver.find_element(By.CSS_SELECTOR, ".d-block").click()

            # Navegar a la lista de espacios
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Espacios"))
            ).click()

            # Encontrar el botón de eliminación del espacio y hacer clic
            eliminar_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".delete-form > .btn"))
            )
            eliminar_button.click()

            # Esperar a que el modal sea visible
            modal = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "confirmDeleteModal"))
            )

            # Esperar a que el campo de confirmación esté visible y escribir el nombre del espacio
            confirm_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "confirmSpaceName"))
            )
            confirm_input.send_keys("Espacio de prueba")

            # Hacer clic en el botón para confirmar la eliminación
            confirm_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "confirmDeleteButton"))
            )
            confirm_button.click()
            
            # Validar que el modal se cerró
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element((By.ID, "confirmModal"))
            )

            # Esperar a que el espacio sea eliminado
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.LINK_TEXT, "Espacio de prueba"))
            )

            # Verificar que el espacio ha sido eliminado
            WebDriverWait(driver, 10).until(
                EC.url_contains("espacios/list")
            )
            print("Eliminación completada exitosamente.")

        except Exception as e:
            # Guardar captura de pantalla solo si la ventana sigue abierta
            if driver.current_window_handle:
                driver.save_screenshot("error_eliminar_screenshot.png")
            self.fail(f"Error durante la prueba de eliminación: {e}")


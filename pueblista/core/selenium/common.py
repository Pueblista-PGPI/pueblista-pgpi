from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def launch_chrome():
    """
    Lanza una nueva instancia de Google Chrome con las opciones necesarias.
    """
    options = Options()
    options.headless = False  # Cambia a True para ejecutar en modo headless (sin interfaz gráfica)

    # Usa webdriver_manager para obtener la última versión de ChromeDriver
    service = Service(ChromeDriverManager().install())

    # Lanza el navegador
    driver = webdriver.Chrome(service=service, options=options)
    return driver
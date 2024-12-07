## Pasos para ejecutar pruebas de cobertura

1. Instalar requirements.txt
   
2. Crear tests para cada módulo en el respectivo `tests.py`
   
3. Ejecutar `coverage run --source=tu_modulo manage.py test tu_modulo` donde `tu_modulo` es el nombre del módulo a testear. 

Si se quiere ejecutar coverage sobre toda la aplicación hay que ejecutar lo siguiente dede la carpeta del proyecto Django: 
 `coverage run --source=. --omit=locustfile.py manage.py test`

4. Ejecutar `coverage report -m` para ver el reporte de cobertura en la terminal
   
5. Ejecutar `coverage html` para generar el reporte de cobertura en un archivo HTML `htmlcov/index.html`

6. Abrir el archivo `htmlcov/index.html`
   
   1. `open htmlcov/index.html` en MacOS
   
   2. `start htmlcov/index.html` en Windows

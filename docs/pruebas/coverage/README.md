## Pasos para ejecutar pruebas de cobertura

1. Instalar requirements.txt
   
2. Crear tests para el módulo en `tests.py`
   
3. Ejecutar `coverage run --source=tu_modulo manage.py test tu_modulo` donde `tu_modulo` es el nombre del módulo a testear
   
4. Ejecutar `coverage report -m` para ver el reporte de cobertura en la terminal
   
5. Ejecutar `coverage html` para generar el reporte de cobertura en un archivo HTML `htmlcov/index.html`

6. Hacer copia de la carpeta `htmlcov` en la carpeta `docs/pruebas/coverage` cambiando el nombre a `modulo_cov`

7. Abrir el archivo `docs/pruebas/coverage/modulo_cov/index.html`
   
   1. `open docs/pruebas/coverage/modulo_cov/index.html` en MacOS
   
   2. `start docs/pruebas/coverage/modulo_cov/index.html` en Windows

**NOTA**: Si alguien es capaz de convertir la carpeta htmlcov a un PDF que lo haga saber, por favor.
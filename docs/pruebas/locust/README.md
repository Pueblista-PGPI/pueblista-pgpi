## Pasos para ejecutar pruebas de cobertura

1. Instalar requirements.txt
   
2. Crear tests para cada módulo en su respectiva clase en  `locustfile.py`
   
3. Ejecutar `locust -f locustfile.py --host=https://pueblista-pgpi.onrender.com/`

4. Acceder a `http://localhost:8089` y selecionar 20 usuarios y la url `https://pueblista-pgpi.onrender.com/` si no llegase a aparecer.
   
5. Ver los informes dentro de la aplicación de locust y comprobar los errores y los logs. 

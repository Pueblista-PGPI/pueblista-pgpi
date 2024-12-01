
# Informe de Testing - Aplicación de Reservas

## 1. Resumen Ejecutivo
- **Objetivo del testing**: El objetivo de las pruebas ha sido comprobar todos los aspectos de la aplicación, desde el punto de vista de la funcionalidad, el rendimiento, la seguridad, etc.
- **Estado general**: Todas las pruebas realizadas fueron exitosas, tanto las pruebas unitarias como las de carga (Locust), como las de interfaz (Selenium). 
- **Principales hallazgos**: Durante el testing no se encontró ningún problema que nos limitase a la hora de probar todas las funcionalidades principales de la aplicación.

## 2. Alcance del Testing
- **Módulos o características probadas**: CRUDs de espacios públicos, de resevas (en espacios normales y espacios especiales), de notificaciones y  de usuarios. Aparte también se han probado el login y las restricciones para acceder a unas vistas u otras. 

Cabe destacar también las pruebas de todos los escenarios positivos y negativos de las características descritas anteriormente, tratando de llegar a la máxima cobertura de código posible. 
- **Tipos de pruebas realizadas**:
  - Unitaria.
  - Interfaz de usuario (UI).
  - Rendimiento/carga.

## 3. Estadísticas Generales

### Número total de casos de prueba ejecutados:
- **Total de pruebas planeadas** 100.
- **Total de pruebas ejecutadas**128.
- **Total de pruebas exitosas**128.

### Porcentaje de éxito:
Fórmula: `(Pruebas exitosas / Total pruebas ejecutadas) * 100`

Aplicando esta fórmula a nuestros datos el porcentaje de éxito es del 100%.

| **Tipo de Prueba** | **Planeadas** | **Ejecutadas** | **Exitosas** | **Porcentaje de éxito** |
|---------------------|---------------|----------------|--------------|--------------------------|
| Unitarias           | 80            | 107            | 107           | 100%                      |
| UI                  | 10            | X             | 10           | 97%                      |
| Carga               | 10             |  19             | 19            | 100%                      |

## 4. Cobertura de Código

- **Porcentaje de cobertura de código**: El porcentaje de cobertura de código indicará la cantidad de líneas que se prueban en el conjunto de tests unitario. Si este es mayor que el 90% se considerará satisfactorio, superando así los estándares de calidad establecidos.
- **Herramientas**: Se usa la herramienta `coverage.py` para probar este dato.

### Aplicación pueblista

- **Cobertura total**: 97%
- **Módulos más críticos**: No hay ningún módulo principal que baje del 90% por lo que no hay módulos críticos.

## 5. Pruebas de Carga y Rendimiento
- **Herramientas utilizadas**: Para las pruebas de carga y rendimiento la herramienta utilizada es Locust. 
- **Resultados clave**:
  - Tiempo promedio de respuesta: 10 ms
  - Máximo número de usuarios concurrentes soportados: 20
  

Se han probado varios módulos todos con la misma cantidad de usuarios concurrentes (20). Las aplicaciones probadas han sido la gestión de espacios, la gestión de reservas, la gestión de usuarios y la homepage. 
Dichas aplicaciones han tenido un tiempo de respuesta bastante positivo, ninguno superando el segundo de retraso. 


## 6. Resultados Detallados

Los resultados detallados se encuentran en formato html y pdf en la carpeta `docs/pruebas/locust`.

## 7. Errores Críticos

No se han producido errores críticos durante el testing. 

## 8. Herramientas y Entorno de Pruebas
- **Herramientas utilizadas**:
  - `coverage` para pruebas unitarias.
  - `selenium` para UI.
  - `Locust` para rendimiento.

- **Entorno**:
  - Sistema operativo (Windows 11).
  - Versión de Django (p. ej., Django 5.1.2).
  - Navegadores probados ( X ).

## 9. Conclusiones y Recomendaciones


**Título**: Informe de Testing - Aplicación de Reservas

**Resumen**:
- Total de pruebas ejecutadas: 128.
- Porcentaje de éxito: 100%.
- Cobertura de código: 97%.
- Pruebas de carga: Soporta 100 usuarios concurrentes con tiempo de respuesta de 500 ms.

**Estadísticas**:

| **Tipo de Prueba** | **Planeadas** | **Ejecutadas** | **Exitosas** | **Porcentaje de éxito** |
|---------------------|---------------|----------------|--------------|--------------------------|
| Unitarias           | 80            | 107             | 107           | 100%                      |
| UI                  | 10            | 30             | 29           | 97%                      |
| Carga               | 10             | 19              | 419           | 100%                      |


**Conclusión**: La aplicación está lista para el despliegue. Todos los tests han sido positivos y con un alto porcentaje de cobertura de código, lo que nos indica que la aplicación es de calidad y que todo funciona correctamente.

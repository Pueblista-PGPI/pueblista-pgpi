---
title: "Informe de pruebas"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "13/10/2024"  # modificar
subject: "PGPI"
author: [Daniel Fernández Caballero, Ramón Gavira Sánchez, José Miguel Iborra Conejo, Antonio Macías Ferrera, Rafael Pulido Cifuentes]
lang: "es"
toc: true
toc-own-page: true
titlepage: true,
titlepage-text-color: "1C1C1C"
titlepage-rule-color: "1C1C1C"
titlepage-rule-height: 0
titlepage-background: "../../../plantilla-markdown/background2V.pdf" # modificar si el doc es horizontal
toc: true
toc-own-page: true
footer-left: "Pueblista - PGPI"
footer-right: "\\thepage"
---

**INFORME DE PRUEBAS**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces
- **CÓDIGO DEL PROYECTO:** 2.15
- **FECHA DE CREACIÓN:** 01/12/2024
- **VERSIÓN DEL DOCUMENTO:** 1.0

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO**

|Fecha	|Realizada por	|Breve descripción de los cambios |
| ----- | ------------- | ----------------- |
|01/12/2024	| Antonio Macías Ferrera, Rafael Pulido Cifuentes |	Elaboración de la primera versión del documento |

\newpage



## RESUMEN EJECUTIVO

- **Objetivo del testing**: El objetivo de las pruebas ha sido comprobar todos los aspectos de la aplicación, desde el punto de vista de la funcionalidad, el rendimiento, la seguridad, etc.
- **Estado general**: Todas las pruebas realizadas fueron exitosas, tanto las pruebas unitarias como las de carga (Locust), como las de interfaz (Selenium). 
- **Principales hallazgos**: Durante el testing no se encontró ningún problema que nos limitase a la hora de probar todas las funcionalidades principales de la aplicación.

## ALCANCE DEL TESTING 

- **Módulos o características probadas**: CRUDs de espacios públicos, de resevas (en espacios normales y espacios especiales), de notificaciones y  de usuarios. Aparte también se han probado el login y las restricciones para acceder a unas vistas u otras. 

Cabe destacar también las pruebas de todos los escenarios positivos y negativos de las características descritas anteriormente, tratando de llegar a la máxima cobertura de código posible. 
- **Tipos de pruebas realizadas**:
  - Unitaria.
  - Interfaz de usuario (UI).
  - Rendimiento/carga.

## ESTADÍSTICAS GENERALES

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

## COBERTURA DE CÓDIGO

- **Porcentaje de cobertura de código**: El porcentaje de cobertura de código indicará la cantidad de líneas que se prueban en el conjunto de tests unitario. Si este es mayor que el 90% se considerará satisfactorio, superando así los estándares de calidad establecidos.
- **Herramientas**: Se usa la herramienta `coverage.py` para probar este dato.

Para acceder al .html detallado se encuentra `docs/pruebas/coverage/modulo_cov/index.html`. A continuación se dirá un resumen de las pruebas realizadas en cada módulo con su porcenaje de cobertura para dar una visión general:

### Módulo de gestión de espacios

- **Número de pruebas**: 18
- **Porcentaje de cobertura**: 96%
- **Descripción de las pruebas**: En las pruebas se ha probado tanto las vistas como el modelo de los espacios públicos. Respecto al modelo se ha probado a crear, editar (tanto parcialmente como completo) y borrar espacios. Para las vistas se han probado las vistas correspondientes a listar, crear, editar con fotos, editar sin fotos, borrar y algunos casos negativos. Todo esto ayuda a que el porcentaje de cobertura del archivo `models.py` sea del 89% y el de `views.py` sea del 91%.  


![cobertura_gestion_espacios](/docs/img/report_cobertura_espacios.png)

### Módulo de gestión de usuarios

- **Número de pruebas**: 27
- **Porcentaje de cobertura**: 100%
- **Descripción de las pruebas**: En las pruebas se ha probado tanto las vistas como el modelo de los distintos usuarios. También cabe recalcar las pruebas relacionadas con la autenticación, que ayudan a que la cobertura sea del 100%. En cuanto a la autenticación se han probado casos positivos y negativos para autenticarse.Con el modelo se ha probado a crear superusuarios con sus correspondientes casos negativos. Para las vistas se han probado las vistas correspondientes a iniciar sesión de manera satisfactoria y de manera errónea, cerrar sesión, listar a los usuarios (si se está autorizado y si no se está) y ver el perfil del usuario autenticado. Debido a todos estos casos de prueba se ha conseguido un 100% de cobertura tanto para el archivo `models.py` como para el archivo `views.py`.

![cobertura_gestion_usuarios](/docs/img/report_cobertura_usuarios.png)

### Módulo de gestión de reservas

- **Número de pruebas**: 39
- **Porcentaje de cobertura**: 96%
- **Descripción de las pruebas**: Puesto que la gestión de las reservas es el centro de nuestra aplicación se han realizado una mayor cantidad de pruebas, con el objetivo de comprobar el mayor número de posibilidades distintas a la hora de ejecutar las funciones. Se ha probado todos los métodos de los modelos de reservas, tanto normal como especial, sus solicitudes, creación, eliminación, edición y todos los correspondientes casos positivos y negativos. Como resultado esto nos da un 100% de cobertura en el archivo de `models.py`. Para finalizar, como ya se ha mencionado previamente se han probado todas las combinaciones posibles de obtener reservas, editar reservas, cancelarlas, solicitar reservas, realizar reservas especiales, obtener el calendario y borrarlas entre otras funciones. Con todo esto, el porcentaje de cobertura de código del archivo `views.py` es del 90%, un muy buen número teniendo en cuenta la extensión de este archivo.

![cobertura_gestion_reservas](/docs/img/report_cobertura_reservas.png)


### Módulo de gestión de notificaciones

- **Número de pruebas**: 7
- **Porcentaje de cobertura**: 99%
- **Descripción de las pruebas**: Al ser un módulo más sencillo solamente se ha probado el CRUD de las notificaciones, tanto para el modelo como para las vistas y el marcar como leída una notificación (un caso particular de edición). Esto nos lleva a obtener un 100% de cobertura tanto en el archivo `models.py` como en el archivo `views.py`.  

![cobertura_gestion_notificaciones](/docs/img/report_cobertura_notificaciones.png)

### Módulo home

- **Número de pruebas**: 10
- **Porcentaje de cobertura**: 98%
- **Descripción de las pruebas**: Para los modelos simplemente se ha probado crear y borrar los posts de información del ayuntamiento. Para las vistas se han probado las funcionalidades para obtener la página principal, editar la información del ayuntamiento, añadir información de ayuntamiento y el envío de correos de dudas o sugerencias. En el archivo `models.py` se ha conseguido una cobertura de un 100% mientras que para el archivo de `views.py` se ha conseguido una cobertura de código de un 95%. 


![cobertura_home](/docs/img/cobertura_home.png)


### Resumen de cobertura

- **Cobertura total**: 97%
- **Módulos más críticos**: No hay ningún módulo principal que baje del 90% por lo que no hay módulos críticos.

## PRUEBAS DE CARGA Y RENDIMIENTO
- **Herramientas utilizadas**: Para las pruebas de carga y rendimiento la herramienta utilizada es Locust. 
- **Resultados clave**:

  - media de peticiones por segundo: 4
  
![prueba_carga_requests](/docs/img/prueba_carga_requests.png)

  - Tiempo promedio de respuesta: 10 ms
  
![response_times](/docs/img/response_times.png)

  - Máximo número de usuarios concurrentes soportados: 20

![numero_usuarios](/docs/img/numero_usuarios.png)

Se han probado varios módulos todos con la misma cantidad de usuarios concurrentes (20). Las aplicaciones probadas han sido la gestión de espacios, la gestión de reservas, la gestión de usuarios y la homepage. 
Dichas aplicaciones han tenido un tiempo de respuesta bastante positivo, ninguno superando el segundo de retraso. 

Los métodos probados con locust con su correspondiente porcentaje de importancia serían los siguientes:

![final_ratio](/docs/img/final_ratio.png)

## RESULTADOS DETALLADOS

Los resultados detallados se encuentran en formato html y pdf en la carpeta `docs/pruebas/locust`.

## ERRORES CRÍTICOS

No se han producido errores críticos durante el testing. 

## HERRAMIENTAS Y ENTORNO DE PRUEBAS

- **Herramientas utilizadas**:
  - `coverage` para pruebas unitarias.
  - `selenium` para UI.
  - `Locust` para rendimiento.

- **Entorno**:
  - Sistema operativo (Windows 11).
  - Versión de Django (p. ej., Django 5.1.2).
  - Navegadores probados ( X ).

## CONCLUSIONES Y RECOMENDACIONES

**Título**: Informe de Testing - Aplicación de Reservas

**Resumen**:
- Total de pruebas ejecutadas: 128.
- Porcentaje de éxito: 100%.
- Cobertura de código: 97%.
- Pruebas de carga: Soporta 20 usuarios concurrentes con tiempo de respuesta de 10 ms.

**Estadísticas**:

| **Tipo de Prueba** | **Planeadas** | **Ejecutadas** | **Exitosas** | **Porcentaje de éxito** |
|---------------------|---------------|----------------|--------------|--------------------------|
| Unitarias           | 80            | 107             | 107           | 100%                      |
| UI                  | 10            | 30             | 29           | 97%                      |
| Carga               | 10             | 19              | 419           | 100%                      |


**Conclusión**: La aplicación está lista para el despliegue. Todos los tests han sido positivos y con un alto porcentaje de cobertura de código, lo que nos indica que la aplicación es de calidad y que todo funciona correctamente.

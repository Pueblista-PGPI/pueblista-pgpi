---
title: "Registro de requisitos"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "13/10/2024"  # modificar
subject: "PGPI"
author: [Antonio Macías Ferrera, Rafael Pulido Cifuentes]
lang: "es"
toc: true
toc-own-page: true
titlepage: true,
titlepage-text-color: "1C1C1C"
titlepage-rule-color: "1C1C1C"
titlepage-rule-height: 0
titlepage-background: "../../plantilla-markdown/background2V.pdf" # modificar si el doc es horizontal
toc: true
toc-own-page: true
footer-left: "Pueblista - PGPI"
footer-right: "\\thepage"
---

# MATRIZ DE TRAZABILIDAD DE REQUISITOS

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces
- **CÓDIGO DEL PROYECTO:** 2.15
- **FECHA DE CREACIÓN:** 13/10/2024
- **VERSIÓN DEL DOCUMENTO:** 1.1

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO**

|Fecha	|Realizada por	|Breve descripción de los cambios |
| ----- | ------------- | ----------------- |
|02/10/2024	| Antonio Macías Ferrera, Rafael Pulido Cifuentes |	Elaboración de la primera versión del documento |

\newpage



# <a name="_toc152419725"></a>**1. Requisitos del proyecto**

|**PRQ-001**|**Entrega del proyecto**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|El proyecto debe cumplir con los términos de referencia del contrato suscrito entre las partes, y debe finalizar antes de su fecha límite el 06/12/2024. |
|**Prioridad**|**Must** |
|**Urgencia**||

|**PRQ-002**|**Accesibilidad del sistema**|
| :- | :- |
|**Versión**|1\.1|
|**Autores**|Ramón Gavira Sánchez|
|**Descripción**|El sistema final debe tener un diseño apropiado y fácil de usar acorde a la edad de los ciudadanos de Villanueva de las Cruces y cumplir con el nivel AA de accesibilidad según el estándar WCAG 2.1|
|**Prioridad**|**Must** |
|**Urgencia**||

|**PRQ-003**|**Inicio de sesión** |
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Los ciudadanos usuarios del sistema deben acceder de forma fácil, sin necesidad de correos electrónicos u otros mecanismos más sofisticados |
|**Prioridad**|**Must** |
|**Urgencia**||

|**PRQ-004**|**Información proporcionada**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|El sistema debe proporcionar información actualizada acerca de los horarios y disponibilidad de los espacios de uso común|
|**Prioridad**|**Must** |
|**Urgencia**||

|**PRQ-005**|**Entrega del proyecto**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|El sistema debe permitir a los usuarios tanto reservar los espacios de uso común como cancelar estas reservas.|
|**Prioridad**|**Must** |
|**Urgencia**||


\newpage


# **2. Requisitos del producto**
## **2.1 Requisitos funcionales del sistema**

### **<a name="_toc152419726"></a>2.1.1 Requisitos de información del sistema**

|**IRQ-001**|**Información sobre los usuarios y clientes**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema debe almacenar la información correspondiente a los usuarios. |
|**Prioridad**|**Must**|
|**Datos específicos**|<p>- Nombre</p><p>- Apellidos</p><p>- Teléfono (opcional)</p><p>- DNI</p><p>- Dirección postal</p>|
|**Urgencia**||

|**IRQ-002**|**Información sobre espacios públicos**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema debe almacenar la información de cada uno de los espacios públicos ofertados por el ayuntamiento de la localidad. |
|**Prioridad**|**Must**|
|**Datos específicos**|<p>- Nombre</p><p>- Horario</p><p>- Descripción</p><p>- Fotos</p><p>- Teléfono de atención (opcional)</p><p>- Estado [RESERVADO, LIBRE, INDISPONIBLE]</p>|
|**Urgencia**||

|**IRQ-003**|**Información sobre ayuntamiento**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema debe almacenar la información acerca del ayuntamiento de la localidad.|
|**Prioridad**|**Must**|
|**Datos específicos**|<p>- Localidad</p><p>- Escudo de la localidad o del ayuntamiento</p><p>- Información de interés</p><p>- Teléfono de atención</p><p>- Correo electrónico de asistencia</p><p>- Foto de portada</p>|
|**Urgencia**||

|**IRQ-004**|**Información sobre las reservas**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema debe almacenar las reservas asociadas a cada espacio público. |
|**Prioridad**|**Must** |
|**Datos específicos**|<p>- Fecha de realización</p><p>- Franja horaria seleccionada</p><p>- Estado [REALIZADA, CANCELADA, EN CURSO, FINALIZADA]</p>|
|**Urgencia**||



### <a name="_toc152419727"></a>**2.1.2 Requisitos de reglas de negocio del sistema**

|**CRQ-001**|**Creación de un espacio público**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Solo un administrador del ayuntamiento de la localidad podrá añadir nuevos espacios públicos. |
|**Prioridad**|**Must** |
|**Urgencia**||

|**CRQ-002**|**Modificación de un espacio público**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Solo un administrador del ayuntamiento de la localidad podrá modificar los datos de un espacio público existente. |
|**Prioridad**|**Must** |
|**Urgencia**||

|**CRQ-003**|**Eliminación de un espacio público**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Solo un administrador del ayuntamiento de la localidad podrá eliminar un espacio público existente. |
|**Prioridad**|**Must** |
|**Urgencia**||

|**CRQ-004**|**Acceso a la aplicación**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Un usuario de la aplicación solo podrá acceder a ella si está censado en el ayuntamiento de la localidad. |
|**Prioridad**|**Must** |
|**Urgencia**||

|**CRQ-005**|**Modificación de un usuario**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Un usuario no podrá modificar sus datos, ya que la información de los usuarios que se registren es proporcionada por el ayuntamiento de la localidad. |
|**Prioridad**|**Must** |
|**Urgencia**||

|**CRQ-006**|**Visualización de espacios públicos**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Solo los usuarios censados en la localidad tendrán acceso a consular los espacios públicos de esta. |
|**Prioridad**|**Must** |
|**Urgencia**||

|**CRQ-007**|**Realización de una reserva**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Solo los usuarios censados en la localidad podrán reservar espacios públicos de esta. |
|**Prioridad**|**Must** |
|**Urgencia**||

|**CRQ-008**|**Disponibilidad de un espacio público**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Un usuario podrá realizar la reserva de un espacio público siempre y cuando el espacio esté marcado como LIBRE en la franja horaria seleccionada. |
|**Prioridad**|**Must** |
|**Urgencia**||

|**CRQ-009**|**Modificación de una reserva**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Un usuario sólo podrá modificar los datos de una reserva a su nombre, pudiendo así cambiar la hora de la reserva, el espacio que solicita o bien cancelar la reserva. |
|**Prioridad**|**Must** |
|**Urgencia**||

|**CRQ-010**|**Visualización de las reserva**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Un usuario sólo podrá ver las reserva a su nombre, mientras que un administrador podrá visualizar todas las reservas realizadas en la plataforma. |
|**Prioridad**|**Must** |
|**Urgencia**||

|**CRQ-011**|**Elimincación de los datos**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Un usuario podrá solicitar la eliminación del registro de todas sus reservas presentes y pasadas. |
|**Prioridad**|**Should** |
|**Urgencia**||
|**Comentario**|Otros datos como el DNI o el nombre no podrán ser eliminados ya que realmente pertenecen al censo del ayuntamiento. |

|**CRQ-012**|**Indisponobilidad de un espacio público**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Si un administrador tiene que reservar un espacio público por un evento extraordinario y esto afecta a una reserva ya realizada por un usuario en este u otros espacios públicos, la reserva deberá ser cancelada. |
|**Prioridad**|**Must** |
|**Urgencia**||
|**Comentario**|Del mismo modo, el usuario deberá ser notificado vía SMS y con una alerta dentro de la aplicación. |

### **<a name="_toc152419728"></a>2.1.3 Requisitos de conducta del sistema**

|**COR-001**|**Disponibilidad de los espacios públicos**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Si un espacio público es marcado como INDISPONIBLE por algún evento extraordinario, deberá mostrar una alerta informativa al consultar el espacio dentro de la aplicación. |
|**Prioridad**|**Must** |
|**Urgencia**||










|**COR-002**|**Aceptación del reglamento de protección de datos**|
| :- | :- |
|**Versión**|1\.0|
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|Se deberá pedir el consentimiento del usuario para el tratamiento de sus datos la primera vez que inicie sesión en la aplicación.  |
|**Prioridad**|**Must** |
|**Urgencia**||






## <a name="_toc152419729"></a>**2.2 Requisitos no funcionales del sistema**


### **<a name="_toc152419730"></a>2.2.1 Requisitos de fiabilidad del sistema**

|**NFR - 001**|**Adaptabilidad de la página web**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|La disponibilidad de los espacios debe reflejarse en tiempo real y evitar conflictos de reservas duplicadas o inconsistencias entre usuarios y administradores.|
|**Prioridad**|**Should**|
|**Urgencia**||

### **<a name="_toc152419731"></a>2.2.2 Requisitos de usabilidad del sistema**

|**NFR - 002**|**Adaptabilidad de la página web**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema deberá adaptarse a tipo de dispositivo se acceda a ella, es decir, que tenga un diseño responsive.|
|**Prioridad**|**Should**|
|**Urgencia**||


| **NFR - 003**|**Inicio de session accesible**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El usuario deberá poder acceder a la aplicación de forma fácil, simplemente ingresando su DNI y fecha de nacimiento para poder ser identificado por el censo del ayuntamiento. Los datos serán comprobados en una base de datos proporcionada por el ayuntamiento|
|**Prioridad**|**Must**|
|**Urgencia**||


| **NFR - 004**|**Interfaz accesible**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema deberá contener una interfaz simple e intuitiva, preparada para ser accesible para personas mayores.|
|**Prioridad**|**Must**|
|**Urgencia**||








### **<a name="_toc152419732"></a>2.2.3 Requisitos de mantenibilidad del sistema**

Aunque no nos comprometemos a realizar un despliegue y mantenimiento de la aplicación funcional, nos comprometemos con los siguientes requisitos de mantenibilidad acorde con su prioridad:

| **NFR - 005**|**Mantenibilidad del codigo**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El código fuente del sistema deberá seguir los ‘coding standards’ adecuados al lenguaje de programación, así como deberá estar debidamente organizado y comentado. |
|**Prioridad**|**Could**|
|**Urgencia**||

### **<a name="_toc152419733"></a>2.2.4 Requisitos de eficiencia del sistema**


| **NFR - 006**|**Disponibilidad del sistema**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|La disponibilidad del sistema debe ser del 99%, asegurando un acceso constante a la información de la BD.|
|**Prioridad**|**Could**|
|**Urgencia**||


| **NFR - 007**|**Tiempo de carga de las distintas vistas**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema debe cargar en un tiempo no superior a 1 segundo, llevando consigo únicamente los datos necesarios y pertinentes a cada una de las vistas.|
|**Prioridad**|**Could**|
|**Urgencia**||

| **NFR - 008**|**Tiempo de carga inicial de la web**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema debe cargar en un tiempo no superior a 5 segundos.|
|**Prioridad**|**Could**|
|**Urgencia**||




| **NFR - 009**|**Limitar las solicitudes**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema deberá limitar las solicitudes por minuto, por ejemplo, a 100, para no sufrir un colapso de esta.|
|**Prioridad**|**Could**|
|**Urgencia**||


### **<a name="_toc152419734"></a>2.2.5 Requisitos de portabilidad del sistema**

| **NFR - 010**|**Varios navegadores**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema deberá estar disponible en distintos navegadores, ya pueden ser Chrome, Firefox, etc.|
|**Prioridad**|**Should**|
|**Urgencia**||








### **<a name="_toc152419735"></a>2.2.6 Requisitos de seguridad del sistema**

| **NFR - 011**|**Funcionalidades de las cuentas**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema debe asegurar que cada rol disponible en la web pueda cumplir únicamente sus funciones designadas, sin acceso a las funciones de otros roles.|
|**Prioridad**|**Must**|
|**Urgencia**||


| **NFR - 012**|**Base de datos a prueba de ataques**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema debe estar protegido contra varios tipos de ataques a la base de datos, ya que contendrá información importante, incluyendo datos confidenciales.|
|**Prioridad**|**Should**|
|**Urgencia**||

\newpage

# 3. **Requisitos de la organización**
## **3.1. Requisitos de entrega** 

| **DRQ - 001**|**Formato de entrega del software**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Todo el software desarrollado que se entregue al cliente debe ser entregado en formato comprimido (.zip, .7zip…) |
|**Prioridad**|**Must**|
|**Urgencia**||

| **DRQ - 002**|**Plazos de entrega**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Todos los productos (documentos, software, actas…) deben ser entregados dentro del plazo acordado con el cliente|
|**Prioridad**|**Must**|
|**Urgencia**||

| **DRQ - 003**|**Validación de los entregables**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Todos los productos entregados deben haber sido previamente validados de acuerdo con las métricas establecidas|
|**Prioridad**|**Must**|
|**Urgencia**||

| **DRQ - 004**|**Calidad de los entregables**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Todos los productos entregados deben cumplir los niveles de calidad establecidos.|
|**Prioridad**|**Must**|
|**Urgencia**||

## **3.2. Requisitos de uso de estándares**

| **USR - 001**|**Estándar de seguridad**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Los datos almacenados y transmitidos por la aplicación deben cumplir con los estándares de seguridad especificados en el Reglamento General de Protección de Datos (GDPR) para asegurar la protección de la información sensible.|
|**Prioridad**|**Must**|
|**Urgencia**||


| **USR - 002**|**Estándar de mejora continua**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|El sistema de actividades de mejora continua debe seguir la estructura del Ciclo de Deming, con intención de mejorar los procesos y actividades que se repiten múltiples veces en el cronograma.|
|**Prioridad**|**Should**|
|**Urgencia**||

| **USR - 003**|**Estándar gestión de proyecto**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|A nivel global, todos los procesos del proyecto actual deben seguir el estándar proporcionado por PMBOK.|
|**Prioridad**|**Must**|
|**Urgencia**||

| **USR - 004**|**Estándar de versionado**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Todos los productos software que sean etiquetados con una versión deben seguir el estándar de versionado semántico|
|**Prioridad**|**Should**|
|**Urgencia**||

| **USR - 005**|**Estándar de programación**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Los productos software deben ser desarrollados siguiendo las prácticas de *Pair Programming*|
|**Prioridad**|**Could**|
|**Urgencia**||

## **3.3.  Requisitos de uso de tecnología**
##
| **UTR - 001**|**Lenguaje de desarrollo BackEnd**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Todo el desarrollo BackEnd del proyecto debe realizarse en lenguaje Python |
|**Prioridad**|**Must**|
|**Urgencia**||

| **UTR - 002**|**Lenguaje de desarrollo FrontEnd**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|El desarrollo FrontEnd del proyecto debe realizarse con JavaScript, HTML y CSS|
|**Prioridad**|**Must**|
|**Urgencia**||

| **UTR - 003**|**Framework de desarrollo**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|El desarrollo del proyecto debe realizarse utilizando el Framework Django|
|**Prioridad**|**Must**|
|**Urgencia**||

| **UTR - 004**|**Herramienta de gestión**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|El proyecto debe ser gestionado (cronogramas, recursos, tareas…) utilizando la herramienta MSProject|
|**Prioridad**|**Must**|
|**Urgencia**||

| **UTR - 005**|**Repositorio del proyecto**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Todos los productos software deben ser almacenados en el repositorio del proyecto (pueblista-pgpi)|
|**Prioridad**|**Must**|
|**Urgencia**||

| **UTR - 006**|**Seguimiento del rendimiento**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Para el seguimiento del rendimiento del equipo de desarrollo durante el proyecto se debe hacer uso de la herramienta ZenHub.|
|**Prioridad**|**Must**|
|**Urgencia**||

| **UTR - 007**|**Computación de horas**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Para la computación de las horas efectivas empleadas durante todo el proyecto, cada miembro del equipo deberá usar la herramienta Clockify.|
|**Prioridad**|**Must**|
|**Urgencia**||












## **4. Requisitos de factores ambientales externos**
##
## **4.1. Requisitos legislativos**

| **AFR - 001**|**Ley Orgánica de Protección de Datos Personales y garantía de los derechos digitales**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Antonio Macías Ferrera|
|**Descripción**|El sistema deberá cumplir la Ley Orgánica de Protección de Datos Personales y garantía de los derechos digitales, ya que registrará bastantes datos personales.|
|**Prioridad**|**Must**|
|**Urgencia**||












## **4.2. Requisitos de privacidad**
##
| **PRR - 001**|**Acceso y control de datos**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|El sistema debe permitir a los usuarios acceder a su perfil de datos y solicitar su eliminación|
|**Prioridad**|**Must**|
|**Urgencia**||

| **PRR - 002**|**Uso de los datos**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Los datos recopilados solo deben utilizarse como método de identificación del usuario como persona censada en el pueblo y no se compartirán con terceros sin el consentimiento del usuario|
|**Prioridad**|**Must**|

| **PRR - 003**|**Almacenamiento y seguridad de datos**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|Los datos personales deben ser almacenados en servidores seguros y se aplicarán controles de acceso para garantizar su seguridad|
|**Prioridad**|**Must**|

| **PRR - 004**|**Notificación de violaciones de datos**|
| - | - |
|**Versión**|1\.0 |
|**Autores**|Rafael Pulido Cifuentes|
|**Descripción**|En caso de violación de datos, se debe notificar a los usuarios dentro de las 72 horas posteriores a la detección de la brecha|
|**Prioridad**|**Must**|


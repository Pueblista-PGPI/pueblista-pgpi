---
title: "Plan de Dirección del Proyecto"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "10/10/2024"  # modificar
subject: "PGPI"
author: [Daniel Fernández Caballero, Ramón Gavira Sánchez, José Miguel Iborra Conejo, Antonio Macías Ferrera, Rafael Pulido Cifuentes]
lang: "es"
toc: true
toc-own-page: false
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

**PLAN DE DIRECCIÓN DEL PROYECTO**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces 
- **CÓDIGO DEL PROYECTO:** 2.15
- **PROPIETARIO DEL PROYECTO:** Ayuntamiento de Villanueva de las Cruces
- **PATROCINADOR DEL PROYECTO:** María José Escalona (alcaldesa)
- **DIRECTOR DEL PROYECTO:** Ramón Gavira Sánchez
- **FECHA DE CREACIÓN:** 11/10/2024
- **ELABORADO POR:** Ramón Gavira Sánchez
- **VERSIÓN DEL DOCUMENTO:** 1.0

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO** 

| Fecha       | Realizada por | Breve descripción de los cambios |
|-------------|---------------|----------------------------------|
|10/10/24             | Ramón Gavira Sánchez              |   Inicio del Plan del Proyecto.                              |
|30/11/24             | Antonio Macías Ferrera            |   Correciones de formato, corrección del Índice.              |


En este documento se desarrolla el Plan de Dirección del Proyecto, como fuente principal de información a consultar en el que se determinará cómo se planificará, ejecutará, supervisará y cerrará el proyecto.

El plan de dirección del proyecto es un documento vivo que irá evolucionando a lo largo del ciclo de vida del proyecto, adaptándose a las necesidades y circunstancias que se vayan presentando. Una vez definidas las líneas base, no será posible modificar el Plan de Proyecto salvo a través de los procesos que queden definidos en el **Plan de Gestión de Cambios**.

\newpage


# 1. OBJETIVOS DEL PROYECTO

| Id  | Objetivo                                                                                                                      |
| --- | ------------------------------------------------------------------------------------------------------------------------------ |
| 001 | El proyecto debe cumplir con los términos de referencia del contrato que se firme con el cliente y debe finalizar antes de la fecha límite 06/12/2024. |
| 002 | Involucrar al cliente en las actividades relevantes del proyecto, para garantizar el éxito de este, obtener un alto grado de satisfacción y confianza de cara a futuros proyectos. |
| 003 | Aumento de la satisfacción de los habitantes del pueblo y un aumento en el uso de estos espacios públicos.                     |
| 004 | Mejorar la eficiencia del pueblo en la gestión de reservas de espacios públicos, reduciendo el tiempo y los recursos necesarios en comparación con el método tradicional de reservas. |
| 005 | Aumentar la adopción de tecnologías digitales en el municipio.   

\newpage

# 2. CICLO DE VIDA DEL PROYECTO

El ciclo de vida del proyecto será un ciclo de vida clásico, en cascada y predictivo. Estará dividido en 4 fases principales: **Inicio, Planificación, Ejecución y Cierre**. Aparentemente será un ciclo de vida en cascada. Cada una de las fases tendrá una serie de tareas que debemos completar antes de pasar a la siguiente fase. Sin embargo, en la fase de **ejecución** se opta por un ciclo de vida ágil, adaptativo e incremental, concretamente se usará la metodología **Scrum**.

El proyecto en esta fase estará organizado en 3 *Sprints* de 1 semana de duración, siendo las fechas de inicio y fin de cada sprint las siguientes:

- **Sprint 1:** 7/11/2024 - 13/11/2024
- **Sprint 2:** 14/11/2024 - 20/11/2024
- **Sprint 3:** 21/11/2024 - 27/11/2024

Cada Sprint tendrá definido un *Sprint Goal* muy claro y definido, que corresponderá a uno de los *hitos* de cada Sprint definidos en el cronograma del proyecto, en concreto serán los siguientes:

| **Código** | **Hito**                                | **Sprint** |
|-------------|-----------------------------------------|------------|
| PUEB01-3.12 | CRUDs de contenidos finalizados          | Sprint 1   |
| PUEB01-3.14 | Gestión de las Reservas finalizada       | Sprint 2   |
| PUEB01-3.17 | Requisitos de conducta operativos        | Sprint 3   |

Todas las tareas de cada Sprint estarán organizadas en el *Product Backlog* y se irán asignando a los *Sprints* según la prioridad, la capacidad del equipo y sobre todo el *Sprint Goal* de cada Sprint. Cada Sprint tendrá su propio *Sprint Planning*, *Sprint Backlog*, *Sprint Review* y *Sprint Retrospective*, y la definición de *Done* de los Sprints será la siguiente:

- La tarea ha sido revisada por un miembro del equipo
- La tarea ha sido probada y funciona correctamente
- Se ha actualizado el estado del tablero de tareas

Para lograrlo haremos especial hincapié en llevar a cabo el testing continuo bajo el enfoque de *Agile Testing*, asegurando así que cada funcionalidad sea probada sin necesidad de esperar a la finalización del sprint y evitando así generar una gran cantidad de documentación de pruebas al final del proyecto.

## 2.1. TABLERO KANBAN

Para la gestión de las tareas de cada Sprint se usará un tablero Kanban, que se actualizará diariamente y que será accesible para todos los miembros del equipo. En este tablero se podrán ver las tareas asignadas a cada miembro del equipo, el estado de cada tarea y el tiempo estimado para completarla.

En la siguiente tabla se detallan las fases del proyecto, las actividades clave, los entregables clave y los criterios de salida de cada fase.

| FASE  | ACTIVIDADES CLAVE | ENTREGABLES CLAVE | CRITERIO DE SALIDA DE LA FASE |
|---------------|-------------------|-------------------|-------------------------------|
| INICIO   | Definir objetivos, identificación de interesados, elaboración del acta de constitución                  |  Acta de constitución                  |  Aprobación del acta de constitución del proyecto                      |
| PLANIFICACIÓN      | Creación del plan de gestión del proyecto, estimación de recursos, identificación y análisis de requisitos, definición del PB                  | Plan de gestión del proyecto, cronograma, PB inicial                   | Aprobación del plan de gestión del Proyecto y entrega del PB                              |
| EJECUCIÓN      | Diseño de prototipos, desarrollo en sprints, revisiones de sprint, testing continuo (agile testing). |  Prototipos validados, producto final e informes de accesibilidad               |  Prototipo validado y cumplimiento de los objetivos de cada sprint y del producto final.                      |
| CIERRE |  Elaboración de manuales y encuestas de satisfacción | Entrega formal del producto, acta de cierre del proyecto, manuales de usuario y administrador, encuestas de satisfacción | Aprobación del acta de cierre del proyecto|

\newpage

# 3. DESVIACIONES AUTORIZADAS (NO GENERAN SOLICITUD DE CAMBIO)
| ASPECTO | UMBRALES |
|--|----------|
| ALCANCE | Se permiten cambios menores en el prototipado sugeridos por el cliente siempre que no impliquen un cambio significativo de los requisitos previamente acordados. Estos cambios deben realizarse antes de iniciar la fase de desarrollo y no deben suponer una ampliación del alcance del producto final. **No se admitirán cambios funcionales que añadan nuevas características o funcionalidades que no hayan sido previamente validadas y aprobadas.**       |
| CRONOGRAMA |  Se autoriza un pequeño desvío en el número de tareas sin finalizar al final de cada sprint, siempre que el retraso no supere el 10% de las tareas planificadas y que la carga de trabajo restante pueda ser redistribuida sin comprometer la entrega final ni generar un impacto en los costos del proyecto. Esta tolerancia no se aplica al último sprint, ya que la fecha de entrega final es inamovible.       |
| PRESUPUESTO |  Se permite una desviación de hasta el 5% del presupuesto total, para cubrir gastos imprevistos menores que no afecten a la ejecución general del proyecto. Esto puede incluir ajustes en materiales, herramientas o servicios que se requieran para mantener el ritmo de trabajo durante los sprints.    |

<br>

# 4. CRITERIOS DE ÉXITO

Tiempo (finalización del proyecto en los plazos requeridos): Se tendrá en cuenta la fecha de finalización del proyecto en comparación con la fecha comprometida. Si la fecha de finalización del proyecto es anterior a la comprometida será un factor de éxito.

Costes: se valorará el coste del proyecto y el ahorro que se consiga. Si el ahorro está entre un 2% y un 5% se considerará un factor de éxito.

Satisfacción del cliente: se valorará el grado de satisfacción del cliente al cierre del proyecto. Si como mínimo es un 8/10 se considerará un éxito

---

Como documentos anexos que son contenido del Plan de Dirección del Proyecto encontramos los siguientes documentos:

\newpage

# 5. DOCUMENTOS ANEXOS

## 5.1. PLANES SUBSIDIARIOS

- PLAN DE GESTIÓN DE REQUISITOS
- PLAN DE GESTIÓN DEL ALCANCE
- PLAN DE GESTIÓN DEL CRONOGRAMA
- PLAN DE GESTIÓN DE COSTES
- PLAN DE GESTIÓN DE CALIDAD
- PLAN DE GESTIÓN DE RECURSOS
- PLAN DE GESTIÓN DE LAS COMUNICACIONES
- PLAN DE GESTIÓN DE RIESGOS
- PLAN DE GESTIÓN DE ADQUISICIONES
- PLAN DE GESTIÓN DE CAMBIOS
- PLAN DE GESTIÓN DE LA CONFIGURACIÓN

## 5.2. LÍNEAS BASE

- LÍNEA BASE DEL ALCANCE: ENUNCIADO DEL ALCANCE, EDT, DICCIONARIO EDT
- LÍNEA BASE DEL CRONOGRAMA: CRONOGRAMA (INFORME MSPROJECT), LISTA DE HITOS
- LÍNEA BASE DEL PRESUPUESTO: PRESUPUESTO (INFORME MSPROJECT)

## 5.3. MATRICES Y REGISTROS

- MATRIZ DE TRAZABILIDAD DE REQUISITOS
- MATRIZ DE ASIGNACIÓN DE RESPONSABILIDADES
- REGISTRO DE REQUISITOS
- REGISTRO DE SUPUESTOS
- REGISTRO DE INTERESADOS
- REGISTRO DE RIESGOS


**APROBACIÓN**

| Cargo               | Firma | Fecha  |
|---------------------|-------|--------|
| Patrocinador        |       |        |
| Director del Proyecto |       |        |

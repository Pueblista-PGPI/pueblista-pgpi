---
title: "Sprint Planning - 3"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "28/11/2024"  # modificar
subject: "PGPI"
author: [Daniel Fernández Caballero, Ramón Gavira Sánchez, José Miguel Iborra Conejo, Antonio Macías Ferrera, Rafael Pulido Cifuentes]
lang: "es"
toc: true
toc-own-page: true
titlepage: true,
titlepage-text-color: "1C1C1C"
titlepage-rule-color: "1C1C1C"
titlepage-rule-height: 0
titlepage-background: "../../../plantilla-markdown/background3V.pdf" # modificar si el doc es horizontal
footer-left: "Pueblista - PGPI"
footer-right: "\\thepage"
documentclass: scrartcl
classoption: "table"        
header-includes:        # para los colores en las tablas
    - \usepackage{colortbl}
    - \usepackage{xcolor}
    - \usepackage{placeins}
---
\definecolor{orange1}{HTML}{EDBB99}
\definecolor{blue1}{HTML}{5DADE2}
\definecolor{green1}{HTML}{52BE80}
\definecolor{purple1}{HTML}{9B59B6}

**ACTA SPRINT PLANNING - 3**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces 
- **CÓDIGO DEL PROYECTO:** 2.15
- **PROPIETARIO DEL PROYECTO:** Ayuntamiento de Villanueva de las cruces
- **PATROCINADOR DEL PROYECTO:** María José Escalona (alcaldesa)
- **DIRECTOR DEL PROYECTO:** Ramón Gavira Sánchez
- **FECHA DE CREACIÓN:** 28/11/2024
- **ELABORADO POR:** Ramón Gavira Sánchez 
- **VERSIÓN DEL DOCUMENTO:** 1.0
 \newline

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO** 

| Fecha       | Realizada por | Breve descripción de los cambios |
|-------------|---------------|----------------------------------|
|28/11/24     | Ramón Gavira Sánchez   | Elaboración de la primera versión del acta del Sprint Planning. |

\newpage

# Objetivo de la Reunión

El objetivo de esta reunión es planificar el trabajo del tercer sprint, seleccionando las tareas del Product Backlog de acuerdo con el Sprint Goal, la prioridad y la capacidad del equipo. Cada sprint contará con su propio Sprint Planning, Sprint Backlog, Sprint Review y Sprint Retrospective. Las tareas de cada sprint se seleccionan siguiendo los criterios de prioridad y capacidad del equipo, y se gestionan en ZenHub.

# Roles del Equipo

- **Scrum Master**: Ramón Gavira Sánchez
- **Equipo de Desarrollo**:
  - Daniel Fernández Caballero
  - José Miguel Iborra Conejo
  - Antonio Macías Ferrera
  - Rafael Pulido Cifuentes

# Objetivo del Sprint (Sprint Goal)

Este último Sprint tiene como objetivo principal entregar la última versión operativa del producto, incluyento todos los requistitos de conducta y de rendimiento. Así como realizar un informe de accesibilidad de acuerdo al estándar WCAG 2.1. AA.

Los hitos y entregables asociados a este Sprint son los siguientes:

- **Identificador del Entregable**: PUEB01-3.22
- **Nombre del Entregable**: Informes de Accesibilidad (AA)
- **Fecha del Entregable**: 25 de noviembre de 2024  
- **Descripción**: El objetivo de este hito es detallar el grado de cumplimiento con el nivel AA de accesibilidad según el estándar WCAG 2.1. Debe incluir una lista de los criterios específicos cumplidos bajo los principios de **perceptible, operable, comprensible y robusto**. Además, se realizará la verificación de accesibilidad en diferentes dispositivos y navegadores, incluyendo tecnologías de asistencia como lectores de pantalla.

- **Identificador del Hito**: PUEB01-3.17
- **Nombre del Hito**: Requisitos de conducta operativos
- **Fecha del Hito**: 27 de noviembre de 2024
- **Descripción**: El objetivo de este hito es llevar a cabo la implementación de los requisitos de conducta operativos que establecerán las pautas de comportamiento y uso adecuado del sistema, asegurando que los usuarios operen dentro de los lineamientos previstos. Esto incluye la configuración de restricciones y avisos dentro del sistema para notificar a los usuarios sobre las acciones que no están permitidas, garantizando así un uso correcto y seguro de la aplicación.

Siguiendo con la línea de los Sprints anteriores, el *Sprint Goal* de este Sprint es el Hito **PUEB01-3.17**, todas las tareas del Sprint Backlog estarán orientadas a cumplir con este objetivo.


# Definición de Hecho (Definition of Done)

La definición de hecho sigue siendo la misma que en los sprints anteriores, todas las tareas deben cumplir con los siguientes criterios:

Todas las tareas de cada Sprint estarán organizadas en el *Product Backlog* y se irán asignando a los *Sprints* según la prioridad, la capacidad del equipo y sobre todo el *Sprint Goal* de cada Sprint. Cada Sprint tendrá su propio *Sprint Planning*, *Sprint Backlog*, *Sprint Review* y *Sprint Retrospective*. Para garantizar que cada tarea cumple con los estándares de calidad del proyecto, hemos establecido la siguiente Definition of Done (DoD):

- La tarea ha sido revisada por un miembro del equipo.
- La tarea ha sido probada y funciona correctamente.
- El estado de la tarea ha sido actualizado en el tablero de ZenHub.

# Gestión de Tareas y Herramientas Utilizadas

Utilizamos ZenHub para la organización del flujo de trabajo y Clockify para el seguimiento del tiempo dedicado a cada tarea. Las columnas de nuestro tablero en ZenHub son las siguientes:

- **Product Backlog**: Tareas pendientes de priorización para sprints futuros.
- **Sprint Backlog**: Tareas seleccionadas para ser trabajadas en el sprint actual.
- **In Progress**: Tareas en las que el equipo está trabajando activamente.
- **Review/QA**: Tareas completadas que están en revisión para verificar el cumplimiento de calidad.
- **Done**: Tareas terminadas que cumplen con la Definition of Done.
- **Closed**: Tareas que han sido completamente terminadas y archivadas.

## Pasos de Gestión de Tareas

1. **Crear y seleccionar tareas** en el *Product Backlog*, asignando tareas específicas al *Sprint Backlog* de acuerdo con las prioridades y capacidades del equipo.
2. **Estimar el esfuerzo** de cada tarea usando Story Points y colocar las tareas en la columna **To Do** al inicio del sprint.
3. Cuando un miembro del equipo inicia una tarea, la mueve a la columna **In Progress** en ZenHub y actualiza Clockify con el tiempo dedicado.
4. Tras completar una tarea, el miembro la mueve a la columna **Review** para revisión y verificación de calidad antes de marcarla como **Done**.

# Estimación del Esfuerzo

Para estimar el esfuerzo utilizaremos **Story Points**, siendo 1 Story Point el esfuerzo mínimo, en el grupo hemos establecido que debe ser una tarea que conlleve no más de una hora, que puedas hacerla de una sentada y sin mucho esfuerzo. Por ahora se han estimado la mayoría de las tareas del Sprint Backlog, no obstante esta planificación puede cambiar en función de las necesidades del equipo, añadiendo más tareas si fuese necesario dividir el trabajo en tareas más pequeñas.

A continuación se muestra una tabla en la que estimamos el esfuerzo de las tareas creadas para cada épica del sprint backlog. (Estas tareas han quedado reflejadas en el tablero de ZenHub).

| Tarea                                             | Story Points |
|---------------------------------------------------|--------------|
| Testing espacios                                  | 2            |
| Testing reservas                                  | 3            |
| Testing Homepage                                  | 1            |
| Testing unitarios finales                         | 4            |
| Informes de Testing                               | 4            |
| Tests de carga y rendimiento                      | 2           |
| Videotutoriales (Demo)                            | 4            |
| Revisar funcionalidad fotos en el despliegue      | 2            |
| Manuales de usuario (Personal Administrativo)            | 2.5            |
| Manuales de usuario (Usuarios Finales)            | 2.5            |
| Mejora de UI/UX                                   | 4            |
| Modificar el diseño para la accesibilidad         | 4            |
| Notificaciones en la aplicación                   | 3            |
| Revisión del backend                              | 3            |
| Informe de Accesibilidad (AA)                     | 2           |
| Tests de UI                                      | 2            |
| Creación de Subespacios                         | 4            |



**Total estimado del Sprint**: 49 Story Points

La estimación de este Sprint, en comparación al resto tiene una desviación de unos 10 Story Points, esto se debe a que es el Sprint Final, y que requiere una revisión e implicación mayor, y además se han añadido 6 Story Points de tareas que no se completaron en el Sprint anterior.

# Análisis del Gráfico Burndown

A continuación, se presenta el Burndown Chart correspondiente al primer sprint. Este gráfico muestra el trabajo restante en función del tiempo. La línea azul refleja el avance ideal y ajustado, ya que en ZenHub no se consideran los fines de semana, aunque el equipo trabaja también esos días. Este gráfico permite visualizar el progreso del equipo y ayuda a ajustar el ritmo si es necesario.

\begin{figure}
\hspace{-1.25cm}
\includegraphics[width=1.2\textwidth]{../../img/burndown-sprint3.png}
\caption{Imagen Burndown del Tercer Sprint}
\end{figure}
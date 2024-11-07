---
title: "Sprint Planning"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "06/11/2024"  # modificar
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

**Sprint Planning**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces 
- **CÓDIGO DEL PROYECTO:** 2.15
- **PROPIETARIO DEL PROYECTO:** Ayuntamiento de Villanueva de las cruces
- **PATROCINADOR DEL PROYECTO:** María José Escalona (alcaldesa)
- **DIRECTOR DEL PROYECTO:** Ramón Gavira Sánchez
- **FECHA DE CREACIÓN:** 15/10/2024
- **ELABORADO POR:** José Miguel Iborra Conejo
- **VERSIÓN DEL DOCUMENTO:** 1.0
 \newline

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO** 

| Fecha       | Realizada por | Breve descripción de los cambios |
|-------------|---------------|----------------------------------|
|06/11/24     | José Miguel Iborra Conejo     | Elaboración de la primera versión del acta del Sprint Planning. |

\newpage

# Acta de Sprint Planning

## Objetivo de la Reunión

El objetivo de esta reunión es planificar el trabajo del segundo sprint, seleccionando las tareas del Product Backlog de acuerdo con el Sprint Goal, la prioridad y la capacidad del equipo. Cada sprint contará con su propio Sprint Planning, Sprint Backlog, Sprint Review y Sprint Retrospective. Las tareas de cada sprint se seleccionan siguiendo los criterios de prioridad y capacidad del equipo, y se gestionan en ZenHub.

## Roles del Equipo

- **Scrum Master**: Ramón Gavira Sánchez
- **Equipo de Desarrollo**:
  - Daniel Fernández Caballero
  - José Miguel Iborra Conejo
  - Antonio Macías Ferrera
  - Rafael Pulido Cifuentes

## Objetivo del Sprint (Sprint Goal)

Este sprint tiene como objetivo completar el desarrollo de funcionalidades CRUD esenciales para el sistema de reserva de espacios, asegurando que los usuarios puedan interactuar con la aplicación en sus funciones básicas.

- **Fecha del Hito**: 13 de noviembre de 2024 
- **Descripción**: Completar las funcionalidades CRUD, lo cual incluye la creación, edición, visualización y eliminación de espacios y datos de usuarios.

## Definición de Hecho (Definition of Done)

Todas las tareas de cada Sprint estarán organizadas en el *Product Backlog* y se irán asignando a los *Sprints* según la prioridad, la capacidad del equipo y sobre todo el *Sprint Goal* de cada Sprint. Cada Sprint tendrá su propio *Sprint Planning*, *Sprint Backlog*, *Sprint Review* y *Sprint Retrospective*. Para garantizar que cada tarea cumple con los estándares de calidad del proyecto, hemos establecido la siguiente Definition of Done (DoD):

- La tarea ha sido revisada por un miembro del equipo.
- La tarea ha sido probada y funciona correctamente.
- El estado de la tarea ha sido actualizado en el tablero de ZenHub.

## Gestión de Tareas y Herramientas Utilizadas

Utilizamos ZenHub para la organización del flujo de trabajo y Clockify para el seguimiento del tiempo dedicado a cada tarea. Las columnas de nuestro tablero en ZenHub son las siguientes:

- **Product Backlog**: Tareas pendientes de priorización para sprints futuros.
- **Sprint Backlog**: Tareas seleccionadas para ser trabajadas en el sprint actual.
- **In Progress**: Tareas en las que el equipo está trabajando activamente.
- **Review/QA**: Tareas completadas que están en revisión para verificar el cumplimiento de calidad.
- **Done**: Tareas terminadas que cumplen con la Definition of Done.
- **Closed**: Tareas que han sido completamente terminadas y archivadas.

### Pasos de Gestión de Tareas

1. **Crear y seleccionar tareas** en el *Product Backlog*, asignando tareas específicas al *Sprint Backlog* de acuerdo con las prioridades y capacidades del equipo.
2. **Estimar el esfuerzo** de cada tarea usando Story Points y colocar las tareas en la columna **To Do** al inicio del sprint.
3. Cuando un miembro del equipo inicia una tarea, la mueve a la columna **In Progress** en ZenHub y actualiza Clockify con el tiempo dedicado.
4. Tras completar una tarea, el miembro la mueve a la columna **Review** para revisión y verificación de calidad antes de marcarla como **Done**.

## Estimación del Esfuerzo

Para estimar el esfuerzo utilizaremos **Story Points**, siendo 1 Story Point el esfuerzo mínimo, en el grupo hemos establecido que debe ser una tarea que conlleve no más de una hora, que puedas hacerla de una sentada y sin mucho esfuerzo. Por ahora se han estimado la mayoría de las tareas del Sprint Backlog, no obstante esta planificación puede cambiar en función de las necesidades del equipo, añadiendo más tareas si fuese necesario dividir el trabajo en tareas más pequeñas.

A continuación se muestra una tabla en la que estimamos el esfuerzo de las tareas creadas para cada épica del sprint backlog. (Estas tareas han quedado reflejadas en el tablero de ZenHub).

| Tarea                                | Story Points |
|--------------------------------------|--------------|
| Borrado de espacios                  | 2            |
| Creación de espacios                 | 4            |
| Contacto directo a la empresa        | 5            |
| Homepage                             | 2.5          |
| Navbar                               | 1.5          |
| Codacy                               | 1.5          |
| Render                               | 1.5          |
| Datos de los usuarios                | 2            |
| Edición de información sobre ayuntamientos | 1      |
| Información sobre espacios           | 3            |
| Información sobre ayuntamiento       | 1.5          |
| Login simple                         | 4            |
| Listado de usuarios                  | 2            |
| Visualizar perfil                    | 2            |

**Total estimado del Sprint**: 33.5 Story Points

## Análisis del Gráfico Burndown

A continuación, se presenta el Burndown Chart correspondiente al primer sprint. Este gráfico muestra el trabajo restante en función del tiempo. La línea azul refleja el avance ideal y ajustado, ya que en ZenHub no se consideran los fines de semana, aunque el equipo trabaja también esos días. Este gráfico permite visualizar el progreso del equipo y ayuda a ajustar el ritmo si es necesario.

\begin{figure}
\hspace{-4.25cm}
\includegraphics[width=1.4\textwidth]{../../img/burndown_sprint_1.jpg}
\caption{Imagen Burndown del Primer Sprint}
\end{figure}
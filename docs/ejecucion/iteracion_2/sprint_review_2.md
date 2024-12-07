---
title: "Sprint Review - 2"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "21/11/2024"  # modificar
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
    - \usepackage{float}  # añadir este paquete
---
\definecolor{orange1}{HTML}{EDBB99}
\definecolor{blue1}{HTML}{5DADE2}
\definecolor{green1}{HTML}{52BE80}
\definecolor{purple1}{HTML}{9B59B6}

**ACTA SPRINT REVIEW - 2**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces 
- **CÓDIGO DEL PROYECTO:** 2.15
- **PROPIETARIO DEL PROYECTO:** Ayuntamiento de Villanueva de las cruces
- **PATROCINADOR DEL PROYECTO:** María José Escalona (alcaldesa)
- **DIRECTOR DEL PROYECTO:** Ramón Gavira Sánchez
- **FECHA DE CREACIÓN:** 21/11/2024
- **ELABORADO POR:** Ramón Gavira Sánchez
- **VERSIÓN DEL DOCUMENTO:** 1.0
 \newline

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO** 

| Fecha       | Realizada por | Breve descripción de los cambios |
|-------------|---------------|----------------------------------|
|21/11/24     | Ramón Gavira Sánchez     | Elaboración de la primera versión del acta del Sprint Review. |

\newpage

# Resumen del Progreso

## 1. Progreso del proyecto (Burndown Chart)

- **Tareas completadas:** 13/16 (81.25%)
- **Tareas pendientes:** 3

En la siguiente imagen se muestra el Burndown Chart del Sprint:

\begin{figure}[H]
\hspace{-1.25cm}
\includegraphics[width=1.1\textwidth]{../../img/burndown-sprint2-finalizado.png}
\caption{Imagen Burndown del Segundo Sprint}
\end{figure}

En la línea de color celeste se muestra el progreso ideal del Sprint, que incluye los fines de semana. En este Sprint hubo un claro retraso por parte del equipo en el fin de semana, no fue hasta el Lunes que el equipo volvió a trabajar con normalidad. Esto se debe a varios factores:

- **Baja Granularidad de las Tareas:** Algunas tareas no estaban lo suficientemente desglosadas, lo que dificultó su implementación.
- **Problemas técnicos:** Se encontraron problemas técnicos que ralentizaron el desarrollo de algunas funcionalidades.

Aparantemente fue un Sprint con un progreso lento, y ZenHub muestra como en un día se completó un 50% de los puntos de historia planificados, pero realmente esto es resultado de la baja granularidad de las tareas y fruto de todo un fin de semana de trabajo, que no se refleja en el gráfico. 

Aún así, el Sprint no se ha completado al 100%, a pesar de mantenernos desde ese momento cercanos a la línea de trabajo ideal, se han quedado 3 tareas sin completar, relacionadas con el Testing de la aplicación, que pasarán al siguiente Sprint.

| Tarea                                | Story Points | Tiempo real |
|--------------------------------------|--------------|------------------|
| Testing espacios                                  | 2            | - |
| Testing reservas                                  | 3            | - |
| Testing Homepage                                  | 1            | - |


## 2. Cumplimiento de plazos

- **Fechas clave cumplidas:**

    - Gestión de las Reservas : 20/11/2024
    - Segunda versión de la aplicación: 20/11/2024

## 3. Rendimiento de recursos humanos

En cuanto al trabajo realizado en horas, todas las tareas del Sprint se estimaron con un total de 39.5 Story Points, lo que equivale a 39 horas y media de trabajo. 

El equipo ha usado la herramienta *Clockify* para medir el tiempo empleado en cada tarea, y se ha registrado un total de 33 horas y 30 minutos. Nos mantenemos en la misma línea que en el Sprint anterior, esto denota que las tareas han sido convenientemente repartidas en ambos Sprints.

El tiempo de trabajo real estimado fue de 39 horas y 30 minutos , y el tiempo real empleado fue de 33 horas y 30 minutos, al que si le sumamos las horas de las 3 tareas que no se han completado (6 Story Points) nos daría un total de 39 horas y 30 minutos. A pesar de no haber completado el Sprint al 100%, las estimaciones fueron precisas.

## 4. Resumen del trabajo realizado

Este Sprint se centró en la implementación de las funcionalidades de reserva de espacios y gestión de las reservas. Los compañeros Daniel Fernández y Jose Miguel Iborra se encargaron de hacer una primera versión de la gestión de las reservas. Antonio Macías y Rafael Pulido se encargaron de las tareas de revisión que quedaban pendientes y del listado de las reservas.

Por último, el equipo detectó la necesidad de cambiar cierta lógica en las reservas, y sobre todo de implementar un sistema de reservas *especiales*, que permitan a los usuarios reservar espacios de manera especial, como por ejemplo, para eventos o actividades especiales. Ramón Gavira se encargó de esta tarea, y fue la que más desviación tuvo en cuanto a tiempo estimado y tiempo real empleado.

El resto del equipo se encargaba de las tareas de Testing, pero al no haberse completado todas las tareas de implementación y enfrentarnos a problemas técnicos, no fue posible completarlas, y pasarán al siguiente Sprint.

# Tares que pasan al siguiente Sprint

- Testing espacios
- Testing reservas
- Testing Homepage


# Conclusiones

El equipo ha sido capaz de cumplir con todas las tareas planificadas para este Sprint, alcanzando un ritmo de trabajo constante una vez superados los obstáculos iniciales. Se ha demostrado una buena capacidad de organización y de gestión del tiempo, y se ha mantenido una comunicación fluida y efectiva entre los miembros del equipo. 

El trabajo en equipo ha sido fundamental para superar los obstáculos iniciales y para avanzar de manera eficiente en la implementación de las funcionalidades del sistema. En general, el equipo se muestra satisfecho con los resultados obtenidos en este Sprint y se siente motivado para afrontar los nuevos retos que se presentarán en los próximos Sprints.


\newpage

# Anexos

# Anexo 1: Estimación del Esfuerzo

A continuación se muestra una tabla con la estimación del esfuerzo comparado con el tiempo real empleado en cada tarea:

| Tarea                                | Story Points | Tiempo real |
|--------------------------------------|--------------|------------------|
| Reservas por franjas horarias                     | 4.5          | 2 horas |
| Múltiples reservas                                | 2.5          | 1 hora |
| Cancelación de reservas                           | 2.5          | 1 hora |
| Creación de reservas                              | 5            | 6 horas |
| Revisar listado de usuarios                       | 1.5          | 1 hora |
| Testing de usuarios                               | 1.5          | 1 hora |
| Revisar funcionalidad correo de contacto          | 1.5          | 30 minutos |
| Revisión de listado de espacios                   | 1.5          | 1 hora |
| Listado de reservas                               | 4            | 4.5 horas |
| Ver reservas (usuario)                            | 3.5          | 2 horas |
| Revisar direccionamiento de rutas                 | 0.5          | 30 minutos |
| Testing espacios                                  | 2            | - |
| Testing reservas                                  | 3            | - |
| Testing Homepage                                  | 1            | - |
| Reserva especial de espacios                      | 2            | 6 horas |
| Borrado de reservas por reservas de orden superior| 2            | 4 horas |







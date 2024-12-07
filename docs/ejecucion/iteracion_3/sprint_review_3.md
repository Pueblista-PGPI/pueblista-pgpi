---
title: "Sprint Review - 3"  # modificar
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

**ACTA SPRINT REVIEW - 3**

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
|28/11/24     | Ramón Gavira Sánchez     | Elaboración de la primera versión del acta del Sprint Review. |

\newpage

# Resumen del Progreso

## 1. Progreso del proyecto (Burndown Chart)

- **Tareas completadas:** 16/16 (100%)
- **Tareas pendientes:** 0

En la siguiente imagen se muestra el Burndown Chart del Sprint:

\begin{figure}[H]
\hspace{-1.25cm}
\includegraphics[width=1.1\textwidth]{../../img/burndown-sprint3-finalizado.png}
\caption{Imagen Burndown del Tercer Sprint}
\end{figure}

En todo momento del Sprint el equipo ha ido por detrás de la línea de trabajo ideal, aunque finalmente se ha conseguido completar todas las tareas planificadas. La desviación se debe a una revisión exhaustiva de las tareas, que ha impedido que pasen al estado de *Done* hasta que no se ha comprobado que estaban correctamente implementadas, y una constante revisión de las mismas, por ello no fue hasta el mismo míercoles 27 de noviembre que se pudieron cerrar el total de las tareas.

\newpage

## 2. Cumplimiento de plazos

- **Fechas clave cumplidas:**

    - Informes de Accesibilidad: 25/11/2024
    - Requisitos de Conducta operativos: 27/11/2024

## 3. Rendimiento de recursos humanos

En cuanto al trabajo realizado en horas, todas las tareas del Sprint se estimaron con un total de 49 Story Points, lo que equivale a 49 horas y media de trabajo. 

El equipo ha usado la herramienta *Clockify* para medir el tiempo empleado en cada tarea, y se ha registrado un total de 59 horas y 30 minutos. Esto supone una desviación del 20% respecto a la estimación inicial, lo que indica que el equipo ha sido capaz de completar las tareas en un tiempo razonablemente cercano al estimado, este incremento en el tiempo es el causante de la desviación en el Burndown Chart.

## 4. Resumen del trabajo realizado

El trabajo del equipo en este Sprint ha sido muy intenso, y se ha logrado completar todas las tareas planificadas. Se han superado los obstáculos iniciales y se ha alcanzado un ritmo de trabajo constante, lo que ha permitido avanzar de manera eficiente en la implementación de las funcionalidades del sistema. El sistema ha quedado completamente operativo, e incluso se han podido realizar videos demostrativos de su funcionamiento. 

Las tareas no se han limitado en la implementación. Los informes de accesibilidad, testing y manuales de usuario han sido una parte fundamental del Sprint, demostrando la importancia de un equipo multidisciplinar en el desarrollo de un proyecto de estas características, y dandole la importancia que se merece a la accesibilidad y a la documentación de una aplicación web.

# Conclusiones

El Sprint 3 ha sido un éxito rotundo, logrando completar todas las tareas planificadas y cumpliendo con las fechas clave establecidas. A pesar de la desviación en el tiempo estimado para algunas tareas, el equipo ha demostrado una gran capacidad de adaptación y eficiencia en la ejecución de sus responsabilidades. La implementación de funcionalidades, junto con la elaboración de informes de accesibilidad y manuales de usuario, ha sido fundamental para asegurar la calidad y usabilidad del sistema. Este Sprint ha consolidado el trabajo realizado en iteraciones anteriores y ha dejado el proyecto en una posición muy favorable para futuras fases de desarrollo. El producto final ha superado las expectativas iniciales y se encuentra listo para ser entregado al cliente.

\newpage

# Anexos

# Anexo 1: Estimación del Esfuerzo

A continuación se muestra una tabla con la estimación del esfuerzo comparado con el tiempo real empleado en cada tarea:

| Tarea                                | Story Points | Tiempo real |
|--------------------------------------|--------------|------------------|
| Testing espacios                                  | 2            | 1 hora |
| Testing reservas                                  | 3            | 2 horas |
| Testing Homepage                                  | 1            | 1 hora |
| Testing unitarios finales                         | 4            | 2 horas |
| Informes de Testing                               | 4            | 3 horas |
| Tests de carga y rendimiento                      | 2           | 5 horas |
| Videotutoriales (Demo)                            | 4            | 5 horas |
| Revisar funcionalidad fotos en el despliegue      | 2            | 2 horas |
| Manuales de usuario (Personal Administrativo)            | 2.5            | 4 horas |
| Manuales de usuario (Usuarios Finales)            | 2.5            | 3 horas |
| Mejora de UI/UX                                   | 4            | 6  horas |
| Modificar el diseño para la accesibilidad         | 4            | 4 horas |
| Notificaciones en la aplicación                   | 3            | 4  horas |
| Revisión del backend                              | 3            | 4 horas y 30 minutos |
| Informe de Accesibilidad (AA)                     | 2           | 2 horas |
| Tests de UI                                      | 2            | 4 horas |
| Creación de Subespacios                         | 4            | 6 horas |







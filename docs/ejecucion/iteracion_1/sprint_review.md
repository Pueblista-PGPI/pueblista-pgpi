---
title: "Sprint Review - 1"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "14/11/2024"  # modificar
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

**Sprint Review - 1**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces 
- **CÓDIGO DEL PROYECTO:** 2.15
- **PROPIETARIO DEL PROYECTO:** Ayuntamiento de Villanueva de las cruces
- **PATROCINADOR DEL PROYECTO:** María José Escalona (alcaldesa)
- **DIRECTOR DEL PROYECTO:** Ramón Gavira Sánchez
- **FECHA DE CREACIÓN:** 14/11/2024
- **ELABORADO POR:** Ramón Gavira Sánchez
- **VERSIÓN DEL DOCUMENTO:** 1.0
 \newline

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO** 

| Fecha       | Realizada por | Breve descripción de los cambios |
|-------------|---------------|----------------------------------|
|14/11/24     | Ramón Gavira Sánchez     | Elaboración de la primera versión del acta del Sprint Review. |

\newpage


## Resumen del Progreso

### 1. Progreso del proyecto (Burndown Chart)

- **Tareas completadas:** 14/14 (100%)
- **Tareas pendientes:** 0

En la siguiente imagen se muestra el Burndown Chart del Sprint:

\begin{figure}[H]
\hspace{-1.25cm}
\includegraphics[width=1.1\textwidth]{../../img/burndown_finalizado_1.jpg}
\caption{Imagen Burndown del Primer Sprint}
\end{figure}

En la línea de color celeste se muestra el progreso ideal del Sprint, que incluye los fines de semana. Como se puede apreciar al inicio del Sprint hubo un claro bloqueo que impidió el avance del equipo, esto se debe por varios motivos:

- La falta de experiencia del equipo con la tecnología Django.
- Dependencia de la tarea de la creación de la base de datos y los primeros usuarios.

Una vez superados estos obstáculos, el equipo ha sido capaz de avanzar a un ritmo constante y ha sido capaz de completar todas las tareas planificadas, de hecho se ha conseguido mantener el ritmo ideal de progreso.

### 2. Cumplimiento de plazos

- **Fechas clave cumplidas:**
    - Product Backlog: 10/11/2024
    - Entrega de los mockups: 10/11/2024
    - CRUDs de contenidos: 13/11/2024
    - Primera versión de la aplicación: 13/11/2024

### 3. Rendimiento de recursos humanos

En cuanto al trabajo realizado en horas, todas las tareas del Sprint se estimaron con un total de 33.5 Story Points, lo que equivale a 33 horas y media de trabajo. 

El equipo ha usado la herramienta *Clockify* para medir el tiempo empleado en cada tarea, y se ha registrado un total de 31 horas y 51 minutos. La estimación ha sido bastante precisa, y el equipo ha sido capaz de completar todas las tareas en el tiempo previsto.

### 4. Resumen del trabajo realizado

En este Sprint se centró en implementar las primeras funcionalidades del sistema, incluyendo la creación de la base de datos y la creación de los usuarios, que fue lo primero que se realizó para poder avanzar con el resto de tareas. A continuación, se implementaron las funcionalidades CRUD para los espacios disponibles en la aplicación, permitiendo a los usuarios con permisos crear, editar, visualizar y eliminar espacios.

De manera paralela, otra parte del equipo estuvo trabajando en el diseño de los mockups de la aplicación y en mantener un diseño y estructura coherente y atractiva para los usuarios. De manera adicional se dejó la aplicación desplegada y se utilizó un software de análisis de código para asegurar la calidad del código durante el desarrollo.

## Tares de mejora que pasan al siguiente Sprint

De manera general se realizarán tareas de mejora de la mayoría de las funcionalidades, esto no quiere decir que la tarea no esté completada, sino que se pueden mejorar. Además se hará el testing de todo lo que no se pudo testear en este Sprint. En concreto las tareas que pasan al siguiente sprint son:

- Revisar funcionalidad de correo de contacto
- Revisar direccionamiento de rutas
- Revisión listado de espacios
- Revisar listado de usuarios
- Revisar perfil de usuario
- Testing de usuarios
- Testing de espacios
- Testing de la homepage

## Conclusiones

El equipo ha sido capaz de cumplir con todas las tareas planificadas para este Sprint, alcanzando un ritmo de trabajo constante una vez superados los obstáculos iniciales. Se ha demostrado una buena capacidad de organización y de gestión del tiempo, y se ha mantenido una comunicación fluida y efectiva entre los miembros del equipo. 

El trabajo en equipo ha sido fundamental para superar los obstáculos iniciales y para avanzar de manera eficiente en la implementación de las funcionalidades del sistema. En general, el equipo se muestra satisfecho con los resultados obtenidos en este Sprint y se siente motivado para afrontar los nuevos retos que se presentarán en los próximos Sprints.


\newpage

# Anexos

## Anexo 1: Estimación del Esfuerzo

A continuación se muestra una tabla con la estimación del esfuerzo comparado con el tiempo real empleado en cada tarea:

| Tarea                                | Story Points | Tiempo real |
|--------------------------------------|--------------|------------------|
| Borrado de espacios                  | 2            | 2.5 horas |
| Creación de espacios                 | 4            | 3 horas |
| Contacto directo a la empresa        | 5            | 2 horas y 25 minutos |
| Homepage                             | 2.5          | 3 horas y 20 minutos |
| Navbar                               | 1.5          | 1 hora y 10 minutos |
| Codacy                               | 1.5          | 30 minutos |
| Render                               | 1.5          | 3 horas y 30 minutos |
| Datos de los usuarios                | 2            | 2 horas y 5 minutos |
| Edición de información sobre ayuntamientos | 1      | 1 hora y 30 minutos |
| Información sobre espacios           | 3            | 20 minutos |
| Información sobre ayuntamiento       | 1.5          | 1 hora y 30 minutos |
| Login simple                         | 4            | 1 hora y 15 minutos |
| Listado de usuarios                  | 2            | 2 horas y 25 minutos |
| Visualizar perfil                    | 2            | 2 horas |
| Prototipos de la aplicación          | *Fuera del PB*            | 6 horas |

La estimación del esfuerzo se ha visto afectada, ya que realmente los prototipos de la aplicación no estaban en el Product Backlog, pero se han realizado y han sido necesarios para el desarrollo de la aplicación, si no se hubieran contado las horas trabajadas frente a las estimadas habrían sido de 26 frente a las 33.5 estimadas.




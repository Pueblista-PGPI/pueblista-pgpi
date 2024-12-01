---
title: "Matriz de asignación de responsabilidades"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "26/10/2024"  # modificar
subject: "PGPI"
author: [Daniel Fernández Caballero, Ramón Gavira Sánchez, José Miguel Iborra Conejo, Antonio Macías Ferrera, Rafael Pulido Cifuentes]
lang: "es"
titlepage: true,
titlepage-text-color: "1C1C1C"
titlepage-rule-color: "1C1C1C"
titlepage-rule-height: 0
titlepage-background: "../../../plantilla-markdown/background2H.pdf" # modificar si el doc es horizontal
page-background: "../../../plantilla-markdown/background2.pdf" # opcional, para fondo pagina
footer-left: "Pueblista - PGPI"
footer-right: "\\thepage"
documentclass: scrartcl
classoption: "table"        
header-includes:        # para los colores en las tablas
    - \usepackage{colortbl}
    - \usepackage{xcolor}
    - \usepackage{placeins}
    - \usepackage{graphicx}
    - \usepackage{changepage}
---
\definecolor{blue1}{HTML}{5DADE2}


**MATRIZ DE ASIGNACIÓN DE RESPONSABILIDADES**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces 
- **CÓDIGO DEL PROYECTO:** 2.15
- **PROPIETARIO DEL PROYECTO:** Ayuntamiento de Villanueva de las cruces
- **PATROCINADOR DEL PROYECTO:** María José Escalona (alcaldesa)
- **DIRECTOR DEL PROYECTO:** Ramón Gavira Sánchez
- **FECHA DE CREACIÓN:** 26/10/2024
- **ELABORADO POR:** Antonio Macías Ferrera, Ramón Gavira Sánchez
- **VERSIÓN DEL DOCUMENTO:** 1.2 \newline


**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO** 

|Fecha	|Realizada por	|Breve descripción de los cambios
| ----- | ------------- | ----------------- |
| 26/10/2024	|  Daniel Fernández Caballero, Antonio Macías Ferrera	| Elaboración del documento  |
|04/11/2024	| Antonio Macías Ferrera |	Corrección de errores de formato |

\newpage


# MATRIZ DE ASIGNACIÓN DE RESPONSABILIDADES
En el presente documento se detalla la **Matriz de Asignación de Responsabilidades**. Este modelo utiliza un **diagrama o matriz RACI** para establecer de forma clara los roles y responsabilidades de cada miembro del equipo en las diferentes actividades del proyecto. Esto nos permitirá identificar de manera precisa quién es responsable de ejecutar cada tarea, quién tiene la autoridad para aprobar los resultados, quién debe ser consultado para aportar información o validar decisiones, y quién debe ser informado del avance y los resultados. \newline

\setlength{\LTleft}{-3.5cm}
\setlength{\LTright}{0cm}

\begin{longtable}{|>{\raggedright\arraybackslash}p{3.8cm}|p{1.5cm}|p{1.5cm}|p{2cm}|p{2cm}|p{2cm}|p{1.5cm}|p{2cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|}

\hline
\rowcolor{blue1!50}
\textbf{Paquete de Trabajo} & \textbf{Director (PM)} & \textbf{Analista - técnico} & \textbf{Responsable calidad} & \textbf{Responsable comunicación} & \textbf{Responsable riesgos} & \textbf{Analista programador} & \textbf{Programador} & \textbf{Tester} & \textbf{Formador} & \textbf{Diseñador UI/UX} & \textbf{Experto en accesibilidad} \\
\hline

\hline
\textbf{1.1.1 ACTA DE CONSTITUCIÓN} & \textbf{x} & & & & & & & & & & \\
\hline
\textbf{1.1.2 ESTUDIO PREVIO} & \textbf{x} & \textbf{x} & & \textbf{x} & & & & & & & \\
\hline
\textbf{2.1.1 REQUISITOS} & \textbf{x} & \textbf{x} & & \textbf{x} & & & & & & & \\
\hline
\textbf{2.1.2 PLAN COMUNICACIÓN} & \textbf{x} & & & \textbf{x} & & & & & & & \\
\hline
\textbf{2.1.3 GESTIÓN DE ALCANCE} & \textbf{x} & \textbf{x} & & & & & & & & & \\
\hline
\textbf{2.1.4 GESTIÓN DEL CRONOGRAMA} & \textbf{x} & & & & & & & & & & \\
\hline
\textbf{2.1.5 GESTIÓN DE LOS COSTES} & \textbf{x} & & & & & & & & & & \\
\hline
\textbf{2.1.6 GESTIÓN DE LA CALIDAD} & \textbf{x} & & \textbf{x} & & & & & & & & \\
\hline
\textbf{2.1.7 GESTIÓN DE LOS RECURSOS} & \textbf{x} & \textbf{x} & & & & & & & & & \\
\hline
\textbf{2.1.8 GESTIÓN DE ADQUISICIONES} & \textbf{x} & \textbf{x} & & & & & & & & & \\
\hline
\textbf{2.1.9 GESTIÓN DE RIESGOS} & & & & & \textbf{x} & & & & & & \\
\hline
\textbf{2.1.10 GESTIÓN DEL CAMBIO} & \textbf{x} & \textbf{x} & & & & & & & & & \\
\hline
\textbf{3.1.1 MOCK UPS} & \textbf{x} & \textbf{x} & & & & \textbf{x} & & \textbf{x} & \textbf{x} & & \\
\hline
\textbf{3.1.2 CRUDS DE CONTENIDOS} & \textbf{x} & \textbf{x} & & & & \textbf{x} & & \textbf{x} & & & \\
\hline
\textbf{3.2.1 RESERVAS} & & & & & & \textbf{x} & \textbf{x} & \textbf{x} & & \textbf{x} & \textbf{x} \\
\hline
\textbf{3.3.1 REQUISITOS DE CONDUCTA} & & & & & & \textbf{x} & \textbf{x} & \textbf{x} & & \textbf{x} & \textbf{x} \\
\hline
\textbf{3.3.2 INFORMES DE ACCESIBILIDAD} & & & & & & \textbf{x} & \textbf{x} & \textbf{x} & & \textbf{x} & \textbf{x} \\
\hline
\textbf{4.1.1 MANUALES} & \textbf{x} & \textbf{x} & & & & & & & & & \\
\hline
\textbf{4.1.2 ENTREGABLES} & \textbf{x} & \textbf{x} & & & & \textbf{x} & & & & & \\
\hline
\textbf{4.2.1 ENCUESTA DE SATISFACCIÓN} & & & & \textbf{x} & & & & & & & \\
\hline
\textbf{4.2.2 ACTA DE CIERRE} & \textbf{x} & \textbf{x} & & & & & & & & & \\
\hline

\end{longtable}

---
title: "Registro de decisiones"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "26/11/2024"  # modificar
subject: "PGPI"
author: [Daniel Fernández Caballero, Ramón Gavira Sánchez, José Miguel Iborra Conejo, Antonio Macías Ferrera, Rafael Pulido Cifuentes]
lang: "es"
titlepage: true
titlepage-text-color: "1C1C1C"
titlepage-rule-color: "1C1C1C"
titlepage-rule-height: 0
titlepage-background: "../../plantilla-markdown/background3V.pdf" # modificar si el doc es horizontal
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

\definecolor{green1}{HTML}{59A970}
\definecolor{green1!50}{HTML}{A3D4B5}
\definecolor{green1!25}{HTML}{D1E9D8}

**REGISTRO DE DECISIONES**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces 
- **CÓDIGO DEL PROYECTO:** 2.15
- **PROPIETARIO DEL PROYECTO:** Ayuntamiento de Villanueva de las cruces
- **PATROCINADOR DEL PROYECTO:** María José Escalona (alcaldesa)
- **DIRECTOR DEL PROYECTO:** Ramón Gavira Sánchez
- **FECHA DE CREACIÓN:** 26/10/2024
- **ELABORADO POR:** Antonio Macías Ferrera, Ramón Gavira Sánchez
- **VERSIÓN DEL DOCUMENTO:** 1.1 \newline


**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO** 

|Fecha	|Realizada por	|Breve descripción de los cambios
| ----- | ------------- | ----------------- |
| 26/11/2024	|  Ramón Gavira Sánchez, Antonio Macías Ferrera	| Elaboración del documento.  | \newline \newline


\newpage


A lo largo del desarrollo del proyecto se han distinguido dos (2) tipos de decisiones. Se han considerado decisiones todo aquello que no quedó recogido en el documento de requisitos pero que sí están dentro del alcance del proyecto, y que fueron tomadas para poder llegar al objetivo de una manera más eficiente y eficaz.

-	**Decisiones Ejecutivas:** Estas decisiones son tomadas por el Director del Proyecto, con o sin el consenso del Equipo de Dirección del Proyecto. Se trata de decisiones de carácter organizativo que definen cómo se estructura y comporta el equipo, así como las metodologías de trabajo y herramientas que se utilizarán. Este tipo de decisiones suelen tener un impacto global en el desarrollo del proyecto.


-	**Decisiones de implementación:** Incluyen las decisiones adoptadas por uno o varios miembros del equipo de desarrollo para resolver situaciones específicas surgidas durante la ejecución. Estas decisiones se clasifican en dos casos principales:

    - Requisitos incompletos o ambiguos: Cuando un requisito está redactado de manera imprecisa, el desarrollador busca una solución que se considere eficiente dentro de los límites del proyecto.

    - Soluciones a fallos en la implementación: En situaciones en las que la implementación prevista de un requisito no es viable o genera problemas técnicos, el responsable identifica y aplica la solución más adecuada para resolver el inconveniente.

Todas las decisiones tendrán un identificador único y estarán ordenadas por la fecha de decisión, el identificador será DE-X para decisiones ejecutivas y DI-X  para decisiones de implementación, siendo X el número de dicha decisión (comenzando por 001) \newline \newline



## REGISTRO DE DECISIONES EJECUTIVAS

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-001} & Uso de Markdown para documentos oficiales \\
\hline
\textbf{Responsable} & Equipo de Dirección de Proyecto \\
\hline
\textbf{Descripción} & Se descartaron las plantillas oficiales y se decidió utilizar Markdown con estilado LaTeX para mantener uniformidad y calidad en la documentación. \\
\hline
\textbf{Fecha} & 6-10-2024 \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-002} & Pair Programming \\
\hline
\textbf{Responsable} & Director de Proyecto \\
\hline
\textbf{Descripción} & Dada la inexperiencia del equipo, para fomentar la colaboración y retroalimentación entre los miembros, se implementó la técnica de programación por pares, extendida incluso a la documentación. \\
\hline
\textbf{Fecha} & 8-10-2024 \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-003} & Despliegue Continuo \\
\hline
\textbf{Responsable} & Director de Proyecto \\
\hline
\textbf{Descripción} & Se decidió usar la técnica del despliegue continuo (CD) para mantener en todo momento el sistema desplegado en las condiciones de entrega al cliente. \\
\hline
\textbf{Fecha} & 4-11-2024 \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-004} & Integración Continua (Codacy) \\
\hline
\textbf{Responsable} & Director de Proyecto \\
\hline
\textbf{Descripción} & Se decidió integrar Codacy para evaluar el código en cada cambio realizado, asegurando limpieza, control de brechas y estándares de calidad. \\
\hline
\textbf{Fecha} & 4-11-2024 \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-005} & Migración a PostgreSQL \\
\hline
\textbf{Responsable} & Director de Proyecto \\
\hline
\textbf{Descripción} & Debido a las necesidades del despliegue, la base de datos original en SQLite3 fue migrada a PostgreSQL para mejorar el rendimiento y escalabilidad. \\
\hline
\textbf{Fecha} & 12-11-2024 \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-006} & Uso de Render para despliegue continuo \\
\hline
\textbf{Responsable} & Director de Proyecto \\
\hline
\textbf{Descripción} & Tras evaluar servicios como PythonAnywhere, se optó por Render debido a su mejor integración con las necesidades del proyecto y compatibilidad con CD. \\
\hline
\textbf{Fecha} & 12-11-2024 \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-007} & Videotutoriales complementarios (Demos) \\
\hline
\textbf{Responsable} & Director de Proyecto \\
\hline
\textbf{Descripción} & Se decidió complementar los manuales de usuario con videotutoriales explicativos para facilitar la comprensión de las funcionalidades clave. \\
\hline
\textbf{Fecha} & 22-11-2024 \\
\hline
\end{tabular}
\end{table}

. 

\newpage


## REGISTRO DE DECISIONES DE IMPLEMENTACIÓN

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-001} & Uso de Markdown para documentos oficiales \\
\hline
\textbf{Responsable} & Equipo de dirección de proyecto \\
\hline
\textbf{Descripción} & Se descartaron las plantillas oficiales y se decidió utilizar Markdown con estilado LaTeX para mantener uniformidad y calidad en la documentación. \\
\hline
\textbf{Fecha} & 6-10-2024 \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-002} & Pair Programming \\
\hline
\textbf{Responsable} & Director de Proyecto \\
\hline
\textbf{Descripción} & Dada la inexperiencia del equipo, para fomentar la colaboración y retroalimentación entre los miembros, se implementó la técnica de programación por pares, extendida incluso a la documentación. \\
\hline
\textbf{Fecha} & 8-10-2024 \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-003} & Despliegue Continuo \\
\hline
\textbf{Responsable} & Director de Proyecto \\
\hline
\textbf{Descripción} & Se decidió usar la técnica del despliegue continuo (CD) para mantener en todo momento el sistema desplegado en las condiciones de entrega al cliente. \\
\hline
\textbf{Fecha} & 4-11-2024 \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-004} & Integración Continua (Codacy) \\
\hline
\textbf{Responsable} & Director de Proyecto \\
\hline
\textbf{Descripción} & Se decidió integrar Codacy para evaluar el código en cada cambio realizado, asegurando limpieza, control de brechas y estándares de calidad. \\
\hline
\textbf{Fecha} & 4-11-2024 \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-005} & Migración a PostgreSQL \\
\hline
\textbf{Responsable} & Director de Proyecto \\
\hline
\textbf{Descripción} & Debido a las necesidades del despliegue, la base de datos original en SQLite3 fue migrada a PostgreSQL para mejorar el rendimiento y escalabilidad. \\
\hline
\textbf{Fecha} & 12-11-2024 \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-006} & Uso de Render para despliegue continuo \\
\hline
\textbf{Responsable} & Director de Proyecto \\
\hline
\textbf{Descripción} & Tras evaluar servicios como PythonAnywhere, se optó por Render debido a su mejor integración con las necesidades del proyecto y compatibilidad con CD. \\
\hline
\textbf{Fecha} & 12-11-2024 \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{ID} & \textbf{DECISIÓN} \\
\hline
\textbf{DE-007} & Videotutoriales complementarios (Demos) \\
\hline
\textbf{Responsable} & Director de Proyecto \\
\hline
\textbf{Descripción} & Se decidió complementar los manuales de usuario con videotutoriales explicativos para facilitar la comprensión de las funcionalidades clave. \\
\hline
\textbf{Fecha} & 22-11-2024 \\
\hline
\end{tabular}
\end{table}


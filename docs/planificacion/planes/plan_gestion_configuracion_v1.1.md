---
title: "Plan de gestión de la configuración"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "02/11/2024"  # modificar
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
documentclass: scrartcl
classoption: "table"        
header-includes:        # para los colores en las tablas
    - \usepackage{colortbl}
    - \usepackage{xcolor}
    - \usepackage{placeins}
---
\definecolor{blue1}{HTML}{5DADE2}


**PLAN DE GESTIÓN DE LA CONFIGURACIÓN**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces
- **CÓDIGO DEL PROYECTO:** 2.15
- **FECHA DE CREACIÓN:** 02/11/2024
- **VERSIÓN DEL DOCUMENTO:** 1.1 \newline \newline


**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO**

|Fecha	|Realizada por	|Breve descripción de los cambios |
| ----- | ------------- | ----------------- |
|02/11/2024	| Antonio Macías Ferrera, José Miguel Iborra Conejo |	Elaboración de la primera versión del documento |

\newpage



# 1\. NORMAS Y PROCEDIMIENTOS APLICABLES (FAE)  
Este Plan de Gestión de la Configuración se guiará por las metodologías y prácticas establecidas en la **Guía del PMBOK** (Project Management Body of Knowledge), publicada por el Project Management Institute (PMI). 

El plan deberá contener información sobre cómo el equipo de trabajo realizará el seguimiento y control del cambio durante el desarrollo del proyecto, además de cómo se llevará a cabo el control de versiones durante las fases de desarrollo y cierre. Queda excluida del Plan de Gestión de la Configuración la gestión de peticiones y evaluaciones de cambios, que constarán en el correspondiente Plan de Gestión del Cambio. \newline \newline


# 2\. DOCUMENTOS APLICABLES (APO) 
Para la gestión de la configuración podrán ser necesarios los siguientes Activos de Proceso de la Organización (APOs):

1. **Plan de Gestión del Proyecto**: Contiene las directrices generales, cronogramas, riesgos y restricciones que afectan la gestión de la configuración. Sirve como referencia para asegurar que las configuraciones estén alineadas con el alcance y los objetivos del proyecto.
1. **Documentación de Requisitos**: Influye en el plan de configuración, ya que los elementos configurables y sus versiones deben estar en consonancia con los requisitos definidos. 
1. **Plan de Gestión de Cambios**: Como parte de la gestión de la configuración, los cambios en los elementos configurables deben ser gestionados y aprobados. Este plan detalla los procesos de solicitud, revisión y aprobación de cambios en el sistema.
1. **Manual de Usuario y Guía de Instalación**: Estos documentos son relevantes en la configuración, ya que la documentación para el usuario y el entorno de instalación debe reflejar la versión específica y el estado de los componentes en producción.



\newpage


# 3\. ELEMENTOS CONFIGURABLES
Los elementos configurables del proyecto incluyen aquellos artefactos y entregables que pueden estar sujetos a modificaciones durante el desarrollo. Cada uno de estos elementos tendrá un identificador único, y se someterá a control de versiones.

1. **Documento de Requisitos:** define los requisitos del sistema y los criterios de aceptación.

1. **Línea Base del Alcance:** define el alcance aprobado del proyecto.

1. **Línea Base del Cronograma:** contiene el cronograma aprobado, incluyendo los hitos importantes.

1. **Línea Base de Costes:** registra el presupuesto aprobado para el proyecto.

1. **Código Fuente:** código del producto software, sujeto a control de versiones.

1. **Registro de Riesgos:** lista y seguimiento de riesgos identificados en el proyecto.

1. **Registro de Cambios:** documentación de todas las solicitudes de cambio aprobadas.

1. **Hitos de Entrega:** fechas y condiciones para la entrega de los principales hitos del proyecto.





# 4\. ROLES 
Cada rol en el equipo tiene asignadas responsabilidades específicas en la gestión de la configuración, incluyendo la creación, revisión, modificación y control de acceso a los elementos configurables.

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{8cm}|p{4cm}|}
\hline
\rowcolor{blue1!50}
\textbf{ROL} & \textbf{RESPONSABILIDADES} & \textbf{ELEMENTO CONFIGURABLE} \\
\hline
Director de Proyecto & Supervisión general de la configuración y aprobación de cambios críticos. & Todos \\
\hline
Analista Programador & Actualización y control del código fuente. Lidera el equipo de desarrollo. & Código Fuente \\
\hline
Responsable de Calidad & Revisión y auditoría de documentos y líneas base. & Documentos y Línea Base \\
\hline
Responsable de Gestión de Riesgos & Mantenimiento del registro de riesgos y cambios. & Registro de Riesgos y Cambios \\
\hline
Tester & Validación de entregables y verificación de cumplimiento con los requisitos. & Documento de Requisitos \\
\hline
Director Técnico & Aprobación de cambios técnicos en el código fuente. & Código Fuente \\
\hline
\end{tabular}
\end{table}



# 5\. TECNOLOGÍAS A UTILIZAR 
Se emplearán herramientas específicas para la gestión de la configuración, tanto para el almacenamiento y versionado como para el seguimiento de cambios y la colaboración.

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{5cm}|p{6cm}|}
\hline
\rowcolor{blue1!50}
\textbf{ELEMENTO CONFIGURABLE} & \textbf{TECNOLOGÍA} & \textbf{OBSERVACIONES} \\
\hline
Documento de Requisitos & MS Office Suite & Documentación de requisitos y control de versiones en Word. \\
\hline
Línea Base del Alcance & MS Project & Definición y seguimiento del alcance del proyecto. \\
\hline
Línea Base del Cronograma & MS Project, Clockify & Gestión de tiempos y cronograma del proyecto. \\
\hline
Código Fuente & Git, GitHub & Versionado y control de cambios del código fuente del software. \\
\hline
Herramientas de Comunicación & Microsoft Teams (Sharepoint) & Para la entrega y versionado de documentos con el cliente. \\
\hline
\end{tabular}
\end{table}


\newpage


# 6\. CALENDARIO DE INICIO DE CONFIGURACIÓN 

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{1cm}|p{3cm}|p{4cm}|p{6cm}|}
\hline
\rowcolor{blue1!50}
\textbf{\#} & \textbf{Elemento Configurable} & \textbf{Hito} & \textbf{Justificación} \\
\hline
1 & Documento de Requisitos & \textbf{PUEB01-2.22} Requisitos analizados - \textbf{16/10/24} & Establecer los requisitos desde el inicio permite que las configuraciones futuras se basen en necesidades claras y definidas. \\
\hline
2 & Planes & \textbf{PUEB01-2.31} Gestión del cambio, fecha del último plan de la etapa de planificación - \textbf{06/11/24} & La elaboración de los documentos de la Fase de Planificación del proyecto podrá sufrir modificaciones, las cuales deberán estar debidamente indicadas en cada uno de los planes de acuerdo a la política de versionado. \\
\hline
3 & Código Fuente & \textbf{PUEB01-3.13} Sprint 1 - \textbf{13/11/24} \newline \textbf{PUEB01-3.15} Sprint 2 - \textbf{20/11/24} \newline \textbf{PUEB01-3.16} Sprint 3 - \textbf{27/11/24} & Cada Sprint y el entregable final deben seguir una política de versionado, convenciones de commits y estándares de código para asegurar una gestión adecuada de las modificaciones del proyecto.  \\
\hline
4 & Registro de cambios y de riesgos & \textbf{PUEB01-3.16} Sprint 3 - \textbf{27/11/24} & Estos documentos sufrirán modificaciones a lo largo de toda la fase de ejecución del proyecto. Se marca como único hito la fecha del último Sprint. \\
\hline
\end{tabular}
\end{table}


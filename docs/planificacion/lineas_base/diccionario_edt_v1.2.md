---
title: "Diccionario de la EDT"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "15/10/2024"  # modificar
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

**DICCIONARIO DE LA EDT**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces 
- **CÓDIGO DEL PROYECTO:** 2.15
- **PROPIETARIO DEL PROYECTO:** Ayuntamiento de Villanueva de las cruces
- **PATROCINADOR DEL PROYECTO:** María José Escalona (alcaldesa)
- **DIRECTOR DEL PROYECTO:** Ramón Gavira Sánchez
- **FECHA DE CREACIÓN:** 15/10/2024
- **ELABORADO POR:** Antonio Macías Ferrera, Ramón Gavira Sánchez
- **VERSIÓN DEL DOCUMENTO:** 1.0
 \newline

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO** 

| Fecha       | Realizada por | Breve descripción de los cambios |
|-------------|---------------|----------------------------------|
|15/10/24     | Antonio Macías Ferrera, Ramón Gavira Sánchez     | Elaboración de la primera versión del diccionario de la EDT. |

\newpage

# **1. INICIO**

\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{INI-001} & \textbf{Acta de constitución} \\
\hline
\textbf{Fase} & 1. Inicio \\
\hline
\textbf{Responsable} & Equipo de dirección de proyecto, cliente y patrocinador. \\
\hline
\textbf{Descripción} & Elaborar el documento fundamental que formaliza el inicio del proyecto, estableciendo su propósito, objetivos, alcance, principales interesados, hitos... El acta de constitución incluye las expectativas de todas las partes involucradas, asegurando un entendimiento común sobre el proyecto. \\
\hline
\textbf{Entregables} & Acta de constitución \\
\hline
\textbf{Hitos} & - Reunión Kick-off (02/10/2024) <br> - Finalizar acta de constitución (9/10/2024) \\
\hline
\textbf{Criterio de aceptación} & El acta de constitución debe ser revisada y aprobada por el cliente y el patrocinador, y debe reflejar de manera precisa los objetivos y el alcance acordado, asegurando así que todas las partes estén alineadas antes de iniciar el trabajo del proyecto. \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{INI-002} & \textbf{Estudio previo} \\
\hline
\textbf{Fase} & 1. Inicio \\
\hline
\textbf{Responsable} & Equipo de dirección de proyecto, cliente y patrocinador. \\
\hline
\textbf{Descripción} & Evaluación inicial que ayuda a definir el alcance del proyecto y el Plan de Dirección del Proyecto. Se elabora un registro de interesados más profundo y un registro de supuestos de alto nivel. \\
\hline
\textbf{Entregables} & E1. Plan de dirección de proyecto <br> - Registro de Interesados <br> - Registro de Supuestos \\
\hline
\textbf{Hitos} & - Finalizar registro de interesados (9/10/2024) <br> - Finalizar registro de supuestos (9/10/2024) \\
\hline
\textbf{Criterio de aceptación} & -- \\
\hline
\end{tabular}
\end{table}



\FloatBarrier

\newpage



# **2. PLANIFICACIÓN**

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PLA-001} & \textbf{Requisitos} \\
\hline
\textbf{Fase} & 2. Planificación \\
\hline
\textbf{Responsable} & Antonio Macías Ferrera, Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Se definen y se documentan las necesidades y expectativas del cliente con respecto al proyecto. Esto incluye elaborar una gestión de los requisitos y una recopilación de todos los requisitos, tanto funcionales como no funcionales. \\
\hline
\textbf{Entregables} & E2 Informe de análisis de los requisitos <br> - Plan de Gestión de Requisitos <br> - Registro de Requisitos <br> - Matriz de trazabilidad \\
\hline
\textbf{Hitos} & - Fin del Plan de Gestión de Requisitos (11/10/2024) <br> - Registro de Requisitos completado y matriz de trazabilidad (13/10/2024) \\
\hline
\textbf{Criterio de aceptación} & Todos los requisitos deben estar documentados, adecuarse al alcance del Proyecto y validados por los interesados, y la Matriz de Trazabilidad debe estar completa. \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PLA-002} & \textbf{Plan de Comunicación} \\
\hline
\textbf{Fase} & 2. Planificación \\
\hline
\textbf{Responsable} & Jose Miguel Iborra Conejo, Daniel Fernández Caballero \\
\hline
\textbf{Descripción} & Se establece un plan que detalla cómo se gestionará la comunicación con todos los interesados del proyecto. Esto incluye la definición de canales, frecuencia, formato y responsables de cada comunicación. \\
\hline
\textbf{Entregables} & E1. Plan de Dirección de Proyecto <br> - Plan de Gestión de las Comunicaciones. \\
\hline
\textbf{Hitos/Actividades} & - Finalizar plan de gestión de las comunicaciones (13/10/2024) <br> - Realización de actas y plantillas para estándares de comunicación (15/10/2024) \\
\hline
\textbf{Criterio de aceptación} & El plan debe ser aprobado por el equipo de dirección y debe cubrir todas las necesidades de comunicación identificadas. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PLA-003} & \textbf{Gestión del Alcance} \\
\hline
\textbf{Fase} & 2. Planificación \\
\hline
\textbf{Responsable} & Daniel Fernández Caballero, Ramón Gavira, Antonio Macías Ferrera, Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Se debe definir la línea base del alcance, documentar los límites del proyecto, los entregables y creación de la EDT, describiendo cada paquete de trabajo. \\
\hline
\textbf{Entregables} & E1. Plan de Dirección de Proyecto <br> - Plan de Gestión del Alcance <br> - Enunciado del Alcance <br> - EDT + Diccionario. \\
\hline
\textbf{Hitos} & - Alcance definido (16/10/2024) <br> - EDT y diccionario terminados (16/10/2024) \\
\hline
\textbf{Criterio de aceptación} & El plan de alcance debe estar alineado con los objetivos del proyecto y ser aprobado por los interesados clave. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PLA-004} & \textbf{Gestión del cronograma} \\
\hline
\textbf{Fase} & 2. Planificación \\
\hline
\textbf{Responsable} & Antonio Macías Ferrera, Ramón Gavira Sánchez \\
\hline
\textbf{Descripción} & Se establece el cronograma del proyecto, definiendo la lista de hitos y actividades y tiempos de ejecución. Nos apoyaremos en la herramienta MS Project. \\
\hline
\textbf{Entregables} & E1. Plan de Dirección de Proyecto <br> - Plan de gestión del cronograma <br> - Lista de actividades <br> - Lista de Hitos <br> - Cronograma en MS Project. \\
\hline
\textbf{Hitos} & - Cronograma y actividades definidas (24/10/2024) \\
\hline
\textbf{Criterio de aceptación} & El cronograma debe estar aprobado y ajustado a las restricciones de tiempo establecidas en el proyecto. \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PLA-005} & \textbf{Gestión de los costes} \\
\hline
\textbf{Fase} & 2. Planificación \\
\hline
\textbf{Responsable} & Director de Proyecto, Equipo de dirección de Proyecto \\
\hline
\textbf{Descripción} & Se definen los procedimientos y herramientas necesarias para planificar, estimar, gestionar y controlar los costes del proyecto, asegurando que se mantenga dentro del presupuesto establecido. Esto incluye la elaboración de un plan de gestión de los costes y la creación de un presupuesto detallado en MS Project, proporcionando una línea base que servirá de referencia en todo el ciclo de vida del proyecto. \\
\hline
\textbf{Entregables} & E1. Plan de Dirección de Proyecto <br> - Plan de gestión de los costes <br> - Presupuesto en MS Project \\
\hline
\textbf{Hitos} & - Plan de gestión de los costes terminado (27/10/2024) <br> - Desarrollo del presupuesto en Project (31/10/2024) \\
\hline
\textbf{Criterio de aceptación} & Los planes y el presupuesto deben ser aprobados por el equipo de dirección y cumplir en adelante con los criterios definidos, garantizando un control financiero eficiente y la alineación con los objetivos del proyecto. \\
\hline
\end{tabular}
\end{table}




\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PLA-006} & \textbf{Gestión de la calidad} \\
\hline
\textbf{Fase} & 2. Planificación \\
\hline
\textbf{Responsable} & Equipo de dirección del Proyecto \\
\hline
\textbf{Descripción} & Se establecen los estándares de calidad y los procedimientos que se seguirán para asegurar que los entregables cumplan con las expectativas del cliente. \\
\hline
\textbf{Entregables} & E1. Plan de Dirección de Proyecto <br> - Plan de gestión de la calidad \\
\hline
\textbf{Hitos} & - Finalización del plan de gestión de calidad (24/10/2024) \\
\hline
\textbf{Criterio de aceptación} & -- \\
\hline
\end{tabular}
\end{table}





\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PLA-007} & \textbf{Gestión de los recursos} \\
\hline
\textbf{Fase} & 2. Planificación \\
\hline
\textbf{Responsable} & Equipo de dirección del Proyecto \\
\hline
\textbf{Descripción} & Se identifican los recursos humanos, materiales y tecnológicos necesarios para el proyecto, y se define una asignación de las responsabilidades de cada paquete de trabajo y sus respectivas actividades. \\
\hline
\textbf{Entregables} & E1. Plan de Dirección de Proyecto <br> - Plan de gestión de los recursos <br> - Matriz de asignación de responsabilidades \\
\hline
\textbf{Hitos} & - Finalizar plan de gestión de los recursos (31/10/2024) <br> - Matriz de asignación de responsabilidades (31/10/2024) \\
\hline
\textbf{Criterio de aceptación} & -- \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PLA-008} & \textbf{Gestión de adquisiciones} \\
\hline
\textbf{Fase} & 2. Planificación \\
\hline
\textbf{Responsable} & Equipo de dirección del Proyecto \\
\hline
\textbf{Descripción} & Se planifican y gestionan las adquisiciones necesarias para el proyecto, definiendo los procedimientos necesarios para comprar productos, servicios o resultados que se necesiten fuera del equipo de proyecto. \\
\hline
\textbf{Entregables} & E1. Plan de Dirección de Proyecto <br> - Plan de gestión de las adquisiciones \\
\hline
\textbf{Hitos} & - Cierre del Plan de gestión de las adquisiciones (31/10/2024) \\
\hline
\textbf{Criterio de aceptación} & Planes aprobados por el equipo de dirección, y cumplir en adelante con los criterios definidos cuando aplique. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PLA-009} & \textbf{Gestión de los riesgos} \\
\hline
\textbf{Fase} & 2. Planificación \\
\hline
\textbf{Responsable} & Equipo de dirección del Proyecto \\
\hline
\textbf{Descripción} & Se identifican y evalúan los riesgos del proyecto, y se definen planes de respuesta para minimizar su impacto en los objetivos. \\
\hline
\textbf{Entregables} & E1. Plan de Dirección de Proyecto <br> - Plan de gestión de la calidad <br> - Registro de Riesgos \\
\hline
\textbf{Hitos} & - Identificación de riesgos y aprobación de planes (24/10/2024) \\
\hline
\textbf{Criterio de aceptación} & -- \\
\hline
\end{tabular}
\end{table}




\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PLA-010} & \textbf{Gestión del cambio} \\
\hline
\textbf{Fase} & 2. Planificación \\
\hline
\textbf{Responsable} & Equipo de dirección del Proyecto \\
\hline
\textbf{Descripción} & Se establecen los procedimientos para la gestión de cambios y de la configuración del proyecto, asegurando que cualquier ajuste en el alcance, tiempo, coste o especificaciones técnicas sea debidamente evaluado, aprobado y documentado. Esto incluye la creación de un plan para gestionar los cambios que detalla cómo se identificarán, analizarán y autorizarán las modificaciones, así como un plan de gestión de la configuración para controlar la evolución y la integridad de los productos y entregables a lo largo del proyecto. \\
\hline
\textbf{Entregables} & E1. Plan de Dirección de Proyecto <br> - Plan de gestión de cambios <br> - Plan de gestión de la configuración \\
\hline
\textbf{Hitos} & - Cerrar plan de gestión de cambios (31/10/2024) <br> - Cerrar plan de gestión de la configuración (7/11/2024) \\
\hline
\textbf{Criterio de aceptación} & Planes aprobados por el equipo de dirección, y cumplir en adelante con los criterios definidos en ambos planes cuando aplique. \\
\hline
\end{tabular}
\end{table}


\FloatBarrier

\newpage


# **3. EJECUCIÓN**

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{EJE-001} & \textbf{Mock ups} \\
\hline
\textbf{Fase} & 3. Ejecución \\
\hline
\textbf{Responsables} & Equipo de diseño \\
\hline
\textbf{Descripción} & Se debe generar la primera versión funcional de la aplicación con una primera funcionalidad básica ateniendo a los primeros requisitos funcionales de urgencia 1. \\
\hline
\textbf{Entregables} & E3. Versión operativa de la aplicación <br> - Mock ups, prototipos funcionales del proyecto con primera funcionalidad \\
\hline
\textbf{Hitos} & - Review de Sprint 1 (13/11/2024) \\
\hline
\textbf{Criterio de aceptación} & Se deberán completar los siguientes requisitos funcionales de urgencia 1: <br> - IRQ-001: Información sobre los usuarios y clientes <br> - IRQ-002: Información sobre espacios públicos <br> - IRQ-003: Información sobre ayuntamiento <br> - IRQ-004: Información sobre las reservas <br> - CRQ-004: Acceso a la aplicación \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{EJE-002} & \textbf{CRUDs de contenidos} \\
\hline
\textbf{Fase} & 3. Ejecución \\
\hline
\textbf{Responsables} & Equipo de desarrollo \\
\hline
\textbf{Descripción} & En esta segunda iteración del proyecto se deberán completar todos los CRUD del sistema, atendiendo así a la mayoría de los requisitos funcionales de urgencia 2 y completando todos los de urgencia 1. \\
\hline
\textbf{Entregables} & E3. Versión operativa de la aplicación <br> - Versión operativa de la aplicación a fecha del Sprint 1 \\
\hline
\textbf{Hitos} & - Fin de Sprint 1 (15/11/2024) \\
\hline
\textbf{Criterio de aceptación} & Se deberán completar los siguientes requisitos funcionales: <br> - CRQ-001: Creación de un espacio público <br> - CRQ-002: Modificación de un espacio público <br> - CRQ-003: Eliminación de un espacio público <br> - CRQ-005: Modificación de un usuario <br> - CRQ-006: Visualización de espacios públicos <br> - CRQ-011: Eliminación de los datos \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{EJE-003} & \textbf{Reservas} \\
\hline
\textbf{Fase} & 3. Ejecución \\
\hline
\textbf{Responsables} & Equipo de desarrollo \\
\hline
\textbf{Descripción} & En el segundo Sprint se llevarán a cabo la mayoría de los requisitos que tienen mayor carga de trabajo, relacionados con la gestión de las reservas. También se atenderán requisitos de fiabilidad y usabilidad del sistema. \\
\hline
\textbf{Entregables} & E3. Versión operativa de la aplicación <br> - Versión operativa de la aplicación a fecha del Sprint 2 \\
\hline
\textbf{Hitos} & - Fin de Sprint 2 (22/11/2024) \\
\hline
\textbf{Criterio de aceptación} & Se deberán completar los siguientes requisitos funcionales: <br> - CRQ-012: Indisponibilidad de un espacio público <br> - CRQ-007: Realización de una reserva <br> - CRQ-008: Disponibilidad de un espacio público <br> - CRQ-009: Modificación de una reserva <br> - CRQ-010: Visualización de las reservas. Además, se deberán atender requisitos de fiabilidad y usabilidad del sistema. \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{EJE-002} & \textbf{CRUDs de contenidos} \\
\hline
\textbf{Fase} & 3. Ejecución \\
\hline
\textbf{Responsables} & Equipo de desarrollo \\
\hline
\textbf{Descripción} & En esta segunda iteración del proyecto se deberán completar todos los CRUD del sistema, atendiendo así a la mayoría de los requisitos funcionales de urgencia 2 y completando todos los de urgencia 1. \\
\hline
\textbf{Entregables} & E3. Versión operativa de la aplicación <br> - Versión operativa de la aplicación a fecha del Sprint 1 \\
\hline
\textbf{Hitos} & - Fin de Sprint 1 (15/11/2024) \\
\hline
\textbf{Criterio de aceptación} & Se deberán completar los siguientes requisitos funcionales: <br> - CRQ-001: Creación de un espacio público <br> - CRQ-002: Modificación de un espacio público <br> - CRQ-003: Eliminación de un espacio público <br> - CRQ-005: Modificación de un usuario <br> - CRQ-006: Visualización de espacios públicos <br> - CRQ-011: Eliminación de los datos. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{EJE-005} & \textbf{Informes de accesibilidad} \\
\hline
\textbf{Fase} & 3. Ejecución \\
\hline
\textbf{Responsables} & Equipo de expertos en accesibilidad y usabilidad, Ramón Gavira Sánchez \\
\hline
\textbf{Descripción} & Se deberá elaborar un informe acerca del nivel de accesibilidad que alcanza el sistema. Sobre todo, teniendo en cuenta que el diseño debe ser intuitivo y estar pensado acorde a la edad de los ciudadanos de Villanueva de las Cruces. \\
\hline
\textbf{Entregables} & E4. Informes de accesibilidad \\
\hline
\textbf{Hitos} & - Fin de Sprint 3 (29/11/2024) \\
\hline
\textbf{Criterio de aceptación} & - Se debe detallar el grado de cumplimiento con el nivel AA de accesibilidad según el estándar WCAG 2.1. <br> - Debe incluir una lista de los criterios específicos cumplidos bajo los principios de **perceptible, operable, comprensible y robusto**. <br> - Verificación de accesibilidad en **diferentes dispositivos** y navegadores, incluyendo tecnologías de asistencia (lectores de pantalla, dispositivos braille, etc.). \\
\hline
\end{tabular}
\end{table}



\FloatBarrier

\newpage


# **4. CIERRE**

\begin{table}[!ht]
\centering
\rowcolors{1}{purple1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{purple1!50}
\textbf{CIE-001} & \textbf{Manuales} \\
\hline
\textbf{Fase} & 4. Cierre \\
\hline
\textbf{Responsables} & Antonio Macías Ferrera, Rafael Pulido Cifuentes, José Miguel Iborra Conejo \\
\hline
\textbf{Descripción} & Elaboración de manuales de usuario y administrador. Los manuales de usuario mostrarán de forma detallada toda la usabilidad de la aplicación por parte de los usuarios finales, mientras que los manuales de administrador procurarán toda la información necesaria para un correcto despliegue y puesta en marcha de la aplicación en su entorno real, así como información acerca de la gestión de espacios públicos y reservas. \\
\hline
\textbf{Entregables} & E5. Manuales de uso de la aplicación <br> - Manual de usuario <br> - Manual de administrador \\
\hline
\textbf{Hitos} & - Preparación de manuales para el entregable (05/11/2024) \\
\hline
\textbf{Criterio de aceptación} & - Debe entregarse toda la documentación técnica relevante, incluyendo cualquier instrucción para la instalación, configuración y mantenimiento del producto. <br> - La documentación técnica debe ser suficiente para que el equipo de soporte o mantenimiento pueda continuar con el producto sin asistencia adicional. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{purple1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{purple1!50}
\textbf{CIE-002} & \textbf{Entregable} \\
\hline
\textbf{Fase} & 4. Cierre \\
\hline
\textbf{Responsable} & Antonio Macías Ferrera, Ramón Gavira Sánchez \\
\hline
\textbf{Descripción} & Entrega formal del producto. Se entrega el producto en formato comprimido (.zip, .7zip…) junto con los manuales de usuario y administrador. \\
\hline
\textbf{Entregables} & E3. Versión operativa de la aplicación <br> - Versión final de la aplicación \\
\hline
\textbf{Hitos} & - Entrega del producto final (06/11/2024) \\
\hline
\textbf{Criterio de aceptación} & - El archivo comprimido con el producto final debe ser entregado en un formato accesible y correcto, sin errores de compresión ni archivos faltantes. <br> - El producto debe incluir todas las funcionalidades especificadas en los requisitos del proyecto, sin errores críticos. <br> - El producto debe ser revisado y aprobado por el cliente o el Product Owner en una reunión formal de aceptación, confirmando que cumple con las expectativas y los requisitos acordados en el contrato. <br> - El proyecto se ha entregado sin exceder el presupuesto acordado, y cualquier desviación ha sido justificada. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{purple1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{purple1!50}
\textbf{CIE-003} & \textbf{Encuesta de satisfacción} \\
\hline
\textbf{Fase} & 4. Cierre \\
\hline
\textbf{Responsable} & Rafael Pulido Cifuentes, Equipo de desarrollo \\
\hline
\textbf{Descripción} & Elaborar y presentar al Product Owner una encuesta para valorar la calidad del producto entregado, la cumplimentación de los requisitos y la eficiencia en la entrega, entre otros aspectos. \\
\hline
\textbf{Entregables} & E6 Encuesta de satisfacción del proyecto \\
\hline
\textbf{Hitos} & - Preparación de encuestas de satisfacción (05/11/2024) <br> - Entrega del producto final (06/11/2024) \\
\hline
\textbf{Criterio de aceptación} & -- \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{purple1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{purple1!50}
\textbf{CIE-004} & \textbf{Acta de cierre} \\
\hline
\textbf{Fase} & 4. Cierre \\
\hline
\textbf{Responsable} & José Miguel Iborra Conejo, Ramón Gavira Sánchez \\
\hline
\textbf{Descripción} & El documento del acta de cierre debe contener la siguiente información que debe ser comunicada al Product Owner: estado de los entregables, cumplimiento de requisitos del producto, informe de desempeño. \\
\hline
\textbf{Entregables} & E7 Informe de cierre \\
\hline
\textbf{Hitos} & - Entrega del producto final (06/11/2024) <br> - Cierre del proyecto (06/11/2024) \\
\hline
\textbf{Criterio de aceptación} & -- \\
\hline
\end{tabular}
\end{table}

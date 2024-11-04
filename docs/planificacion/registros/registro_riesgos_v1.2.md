---
title: "Registro de riesgos"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "22/10/2024"  # modificar
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

**REGISTRO DE RIESGOS**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces
- **CÓDIGO DEL PROYECTO:** 2.15
- **FECHA DE CREACIÓN:** 22/10/2024
- **VERSIÓN DEL DOCUMENTO:** 1.1
 \newline

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO**

|Fecha	|Realizada por	|Breve descripción de los cambios |
| ----- | ------------- | ----------------- |
|22/10/2024	| Antonio Macías Ferrera, José Miguel Iborra Conejo |	Elaboración de la primera versión del documento |

\newpage



# 1\. Riesgos en la Gestión del Alcance del Proyecto

Estos riesgos están relacionados con la posibilidad de cambios, malentendidos o falta de claridad en los requisitos y objetivos del proyecto. Los problemas en esta área pueden generar desviaciones significativas en el alcance, afectando el éxito final del proyecto.

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RAL-001} & \textbf{Requisitos no cubiertos} \\
\hline
\textbf{Descripción} & Es posible que algunos requisitos del proyecto no se cubran adecuadamente debido a la falta de comunicación o a una recolección incompleta de las necesidades del ayuntamiento, lo que podría generar insatisfacción con el producto final. \\
\hline
\textbf{Probabilidad} & 0.6 \\
\hline
\textbf{Impacto en el coste} & 5 \\
\hline
\textbf{Impacto en el alcance} & 7 \\
\hline
\textbf{Impacto en el tiempo} & 5 \\
\hline
\textbf{Impacto en la calidad} & 5 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Se mantendrán reuniones periódicas con el cliente y se actualizará la matriz de requisitos continuamente para evitar la omisión de requisitos críticos. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RAL-002} & \textbf{Solicitud de nuevos requisitos a mitad de proyecto} \\
\hline
\textbf{Descripción} & El cliente podría solicitar la inclusión de nuevas funcionalidades no previstas inicialmente, afectando el alcance y aumentando el coste y el tiempo del proyecto. \\
\hline
\textbf{Probabilidad} & 0.5 \\
\hline
\textbf{Impacto en el coste} & 7 \\
\hline
\textbf{Impacto en el alcance} & 9 \\
\hline
\textbf{Impacto en el tiempo} & 7 \\
\hline
\textbf{Impacto en la calidad} & 5 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Mantener informado al cliente y definir claramente el alcance inicial con documentos firmados. Evaluar cuidadosamente cada nueva solicitud de cambio. \\
\hline
\end{tabular}
\end{table}



\newpage


# 2\. Riesgos en la Gestión del Cronograma del Proyecto

Son riesgos que afectan los plazos de ejecución y las fechas de entrega del proyecto. Un mal control del cronograma puede causar retrasos que afecten todo el ciclo de vida del proyecto y comprometan los plazos comprometidos con los stakeholders.

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RCR-001} & \textbf{Retraso en la recolección de información} \\
\hline
\textbf{Descripción} & El cliente podría retrasarse en proporcionar la información requerida sobre los espacios y su disponibilidad, afectando el cronograma del proyecto. \\
\hline
\textbf{Probabilidad} & 0.7 \\
\hline
\textbf{Impacto en el coste} & 3 \\
\hline
\textbf{Impacto en el alcance} & 3 \\
\hline
\textbf{Impacto en el tiempo} & 7 \\
\hline
\textbf{Impacto en la calidad} & 3 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Programar reuniones periódicas con el cliente y establecer hitos claros para la entrega de información. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RCR-002} & \textbf{Retraso por falta de aprobación de documentos} \\
\hline
\textbf{Descripción} & Los documentos que deben ser aprobados por el cliente no se revisan a tiempo, lo que genera retrasos en el cronograma del proyecto. \\
\hline
\textbf{Probabilidad} & 0.6 \\
\hline
\textbf{Impacto en el coste} & 3 \\
\hline
\textbf{Impacto en el alcance} & 5 \\
\hline
\textbf{Impacto en el tiempo} & 7 \\
\hline
\textbf{Impacto en la calidad} & 3 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Establecer hitos claros y recordar con antelación al cliente la necesidad de revisión y aprobación. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RCR-003} & \textbf{Desviaciones en el cronograma debido a la replanificación frecuente de sprints} \\
\hline
\textbf{Descripción} & En la metodología Scrum, si las prioridades de los sprints cambian frecuentemente por peticiones del cliente o cambios inesperados en el backlog, esto puede causar desviaciones en el cronograma global del proyecto, afectando los plazos de entrega acordados para las funcionalidades clave. \\
\hline
\textbf{Probabilidad} & 0.6 \\
\hline
\textbf{Impacto en el coste} & 5 \\
\hline
\textbf{Impacto en el alcance} & 7 \\
\hline
\textbf{Impacto en el tiempo} & 7 \\
\hline
\textbf{Impacto en la calidad} & 5 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Mantener revisiones frecuentes con el Product Owner para priorizar y estabilizar el backlog. Revisar los sprints y asegurar que las tareas críticas no sufran cambios bruscos sin una evaluación adecuada. Considerar la flexibilidad de tiempo para iteraciones adicionales en el plan global. \\
\hline
\end{tabular}
\end{table}



\newpage

...

\newpage



# 3\. Riesgos en la Gestión de los Costes del Proyecto

Estos riesgos impactan el presupuesto del proyecto, generando sobrecostos o la necesidad de financiamiento adicional no previsto. Un mal control de los costos puede llevar a la inviabilidad económica del proyecto.

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RCO-001} & \textbf{Personal del equipo sin participación establecida} \\
\hline
\textbf{Descripción} & Parte del equipo no tiene su rol ni participación claramente definida, lo que puede generar sobrecostes y baja eficiencia en el proyecto. \\
\hline
\textbf{Probabilidad} & 0.4 \\
\hline
\textbf{Impacto en el coste} & 5 \\
\hline
\textbf{Impacto en el alcance} & 3 \\
\hline
\textbf{Impacto en el tiempo} & 3 \\
\hline
\textbf{Impacto en la calidad} & 3 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Definir roles y responsabilidades de todos los miembros del equipo conforme al plan de trabajo. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RCO-002} & \textbf{Sobrecosto por infraestructura adicional no prevista} \\
\hline
\textbf{Descripción} & El desarrollo de la aplicación podría requerir una infraestructura adicional (servidores, bases de datos) que no esté contemplada en el presupuesto inicial. \\
\hline
\textbf{Probabilidad} & 0.3 \\
\hline
\textbf{Impacto en el coste} & 7 \\
\hline
\textbf{Impacto en el alcance} & 3 \\
\hline
\textbf{Impacto en el tiempo} & 3 \\
\hline
\textbf{Impacto en la calidad} & 3 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Realizar una evaluación temprana de los recursos tecnológicos necesarios y asegurarse de incluirlos en el presupuesto. \\
\hline
\end{tabular}
\end{table}



\newpage


# 4\. Riesgos en la Gestión de la Calidad del Proyecto

Estos riesgos se relacionan con la capacidad del proyecto para cumplir con los estándares de calidad definidos en los entregables. Un fallo en la calidad puede llevar a la insatisfacción del cliente o la necesidad de reprocesos, aumentando los costos y tiempos del proyecto.

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RCA-001} & \textbf{Aprobación del producto final} \\
\hline
\textbf{Descripción} & Existe el riesgo de que las expectativas del cliente no se comprendan bien, lo que generaría rechazo o insatisfacción con el producto final. \\
\hline
\textbf{Probabilidad} & 0.5 \\
\hline
\textbf{Impacto en el coste} & 5 \\
\hline
\textbf{Impacto en el alcance} & 7 \\
\hline
\textbf{Impacto en el tiempo} & 7 \\
\hline
\textbf{Impacto en la calidad} & 9 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Establecer claramente los criterios de aceptación del producto y garantizar la validación del cliente durante todo el proceso. \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RCA-002} & \textbf{Cambios en los estándares de calidad de servicios de socios} \\
\hline
\textbf{Descripción} & Los proveedores o socios externos podrían modificar sus estándares de calidad durante el proyecto, lo que impactaría en la calidad del producto final. \\
\hline
\textbf{Probabilidad} & 0.4 \\
\hline
\textbf{Impacto en el coste} & 3 \\
\hline
\textbf{Impacto en el alcance} & 3 \\
\hline
\textbf{Impacto en el tiempo} & 5 \\
\hline
\textbf{Impacto en la calidad} & 7 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Monitorear los cambios en los estándares de calidad de los proveedores y adaptarse rápidamente a ellos. \\
\hline
\end{tabular}
\end{table}


\newpage


# 5\. Riesgos en la Gestión de Recursos Humanos

Estos riesgos se relacionan con el equipo de trabajo, sus competencias, disponibilidad, y el clima laboral del proyecto. La falta de motivación o la falta de recursos humanos clave puede poner en riesgo el éxito del proyecto.

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RRH-001} & \textbf{Desmotivación del personal por tareas rutinarias} \\
\hline
\textbf{Descripción} & El equipo puede desmotivarse si realiza tareas repetitivas por periodos prolongados, lo que puede afectar la productividad y la calidad del trabajo. \\
\hline
\textbf{Probabilidad} & 0.4 \\
\hline
\textbf{Impacto en el coste} & 3 \\
\hline
\textbf{Impacto en el alcance} & 3 \\
\hline
\textbf{Impacto en el tiempo} & 5 \\
\hline
\textbf{Impacto en la calidad} & 5 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Establecer un plan de rotación de tareas que permita a los miembros del equipo variar sus responsabilidades. \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RRH-002} & \textbf{Pérdida de conocimiento específico del proyecto} \\
\hline
\textbf{Descripción} & La rotación no deseada de miembros del equipo puede generar la pérdida de conocimiento específico del proyecto, afectando la continuidad. \\
\hline
\textbf{Probabilidad} & 0.3 \\
\hline
\textbf{Impacto en el coste} & 5 \\
\hline
\textbf{Impacto en el alcance} & 3 \\
\hline
\textbf{Impacto en el tiempo} & 7 \\
\hline
\textbf{Impacto en la calidad} & 7 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Distribuir el conocimiento entre varios miembros del equipo y documentar los aspectos críticos del proyecto. \\
\hline
\end{tabular}
\end{table}



\newpage


# 6\. Riesgos en la Gestión de Comunicaciones

Estos riesgos están relacionados con la eficacia de la comunicación entre el equipo del proyecto, los stakeholders y otros interesados. La falta de una adecuada gestión de la información puede llevar a malentendidos o decisiones erróneas.

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RCM-001} & \textbf{Información disponible a destiempo} \\
\hline
\textbf{Descripción} & La información clave necesaria para la ejecución del proyecto podría no estar disponible a tiempo, generando retrasos en la planificación y ejecución. \\
\hline
\textbf{Probabilidad} & 0.5 \\
\hline
\textbf{Impacto en el coste} & 3 \\
\hline
\textbf{Impacto en el alcance} & 3 \\
\hline
\textbf{Impacto en el tiempo} & 7 \\
\hline
\textbf{Impacto en la calidad} & 4 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Definir claramente las fechas y responsables de entregar la información crítica y realizar un seguimiento constante. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RCM-002} & \textbf{Falta de comunicación entre el equipo} \\
\hline
\textbf{Descripción} & La falta de comunicación efectiva entre los diferentes miembros del equipo involucrados en el proyecto puede generar malentendidos, retrasos o errores en la implementación de las tareas, lo que afectaría el cumplimiento de los objetivos del proyecto. \\
\hline
\textbf{Probabilidad} & 0.6 \\
\hline
\textbf{Impacto en el coste} & 3 \\
\hline
\textbf{Impacto en el alcance} & 5 \\
\hline
\textbf{Impacto en el tiempo} & 7 \\
\hline
\textbf{Impacto en la calidad} & 4 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Establecer reuniones regulares de seguimiento entre los equipos, así como promover el uso de herramientas colaborativas de comunicación para asegurar una correcta coordinación y flujo de información. \\
\hline
\end{tabular}
\end{table}


\newpage


# 7\. Riesgos en la Gestión de las Adquisiciones

Estos riesgos se derivan de la compra de bienes y servicios necesarios para completar el proyecto. Problemas en las adquisiciones pueden generar retrasos, sobrecostos o fallos en los materiales o servicios contratados.

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RAD-001} & \textbf{Entorno de desarrollo con configuración diferente al entorno de producción} \\
\hline
\textbf{Descripción} & El entorno de desarrollo puede tener una configuración diferente al entorno de producción final, lo que genera problemas en la transición y calidad del sistema. \\
\hline
\textbf{Probabilidad} & 0.4 \\
\hline
\textbf{Impacto en el coste} & 5 \\
\hline
\textbf{Impacto en el alcance} & 3 \\
\hline
\textbf{Impacto en el tiempo} & 5 \\
\hline
\textbf{Impacto en la calidad} & 7 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Asegurar que el entorno de desarrollo refleje fielmente la configuración del entorno de producción, con las mismas versiones y parámetros. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RAD-002} & \textbf{Adquisición de hardware o licencias no realizada a tiempo} \\
\hline
\textbf{Descripción} & Existe el riesgo de que el hardware o las licencias necesarias para el proyecto no se adquieran en los plazos previstos, lo que podría generar retrasos en las actividades de desarrollo o pruebas que dependan de estos recursos. \\
\hline
\textbf{Probabilidad} & 0.7 \\
\hline
\textbf{Impacto en el coste} & 5 \\
\hline
\textbf{Impacto en el alcance} & 3 \\
\hline
\textbf{Impacto en el tiempo} & 7 \\
\hline
\textbf{Impacto en la calidad} & 3 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Coordinar con el equipo de adquisiciones para iniciar el proceso de compra con antelación, establecer fechas límite claras y realizar seguimientos periódicos para garantizar la entrega a tiempo. \\
\hline
\end{tabular}
\end{table}



\newpage


# 8\. Riesgos en la Gestión de Stakeholders del Proyecto

Estos riesgos se relacionan con la gestión de las expectativas y el involucramiento de las partes interesadas (stakeholders). Si los stakeholders no se gestionan adecuadamente, pueden influir

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RST-001} & \textbf{Insatisfacción del cliente por falta de participación de interesados en la definición del proyecto} \\
\hline
\textbf{Descripción} & Existe el riesgo de que algunos stakeholders clave no participen en la definición inicial del proyecto o no se consideren adecuadamente sus expectativas, lo que podría generar insatisfacción y conflictos durante o al final del proyecto. \\
\hline
\textbf{Probabilidad} & 0.6 \\
\hline
\textbf{Impacto en el coste} & 5 \\
\hline
\textbf{Impacto en el alcance} & 7 \\
\hline
\textbf{Impacto en el tiempo} & 5 \\
\hline
\textbf{Impacto en la calidad} & 7 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Asegurar la participación activa de los stakeholders desde el principio del proyecto y mantenerlos informados sobre posibles cambios en los objetivos y resultados. Realizar reuniones periódicas para validar el progreso y los ajustes. \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{RST-002} & \textbf{Disponibilidad insuficiente del cliente o socios para completar actividades} \\
\hline
\textbf{Descripción} & Los clientes o socios clave pueden no estar disponibles en los momentos necesarios para completar actividades críticas dentro del plazo estimado, lo que podría generar retrasos en el cronograma y afectar el éxito del proyecto. \\
\hline
\textbf{Probabilidad} & 0.7 \\
\hline
\textbf{Impacto en el coste} & 5 \\
\hline
\textbf{Impacto en el alcance} & 7 \\
\hline
\textbf{Impacto en el tiempo} & 9 \\
\hline
\textbf{Impacto en la calidad} & 5 \\
\hline
\textbf{Seguimiento y respuesta} & Mitigar – Informar a los stakeholders sobre las fechas planificadas y la dedicación estimada para cada fase del proyecto con suficiente antelación. Confirmar la disponibilidad real en las fechas planificadas y mantener comunicación continua para asegurar la participación oportuna. \\
\hline
\end{tabular}
\end{table}
---
title: "Plan de Gestión de los riesgos"  # modificar
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


**PLAN DE GESTIÓN DE LOS RIESGOS**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces
- **CÓDIGO DEL PROYECTO:** 2.15
- **FECHA DE CREACIÓN:** 22/10/2024
- **VERSIÓN DEL DOCUMENTO:** 1.1

\\

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO**

|Fecha	|Realizada por	|Breve descripción de los cambios |
| ----- | ------------- | ----------------- |
|22/10/2024	| Antonio Macías Ferrera, José Miguel Iborra Conejo |	Elaboración de la primera versión del documento |

\newpage


# 1\. NORMAS Y PROCEDIMIENTOS APLICABLES

Este Plan de Gestión de Riesgos seguirá de manera estricta los procedimientos, metodologías y mejores prácticas establecidos en la Guía del PMBOK (Project Management Body of Knowledge), publicada por el Project Management Institute (PMI).

Dado que la Guía PMBOK es ampliamente reconocida como un estándar internacional para la gestión de proyectos, las directrices contenidas en ella serán aplicadas para:

- La identificación de riesgos mediante herramientas y técnicas recomendadas.
- El análisis cualitativo y cuantitativo de riesgos para evaluar su probabilidad e impacto.
- La planificación de respuestas a los riesgos para minimizar amenazas y aprovechar oportunidades.
- El seguimiento y control de los riesgos durante todo el ciclo de vida del proyecto.

No se adoptarán normas o procedimientos adicionales fuera de los especificados en la Guía PMBOK, garantizando así una alineación completa con las mejores prácticas reconocidas a nivel global.

# 2\. CATEGORÍAS DE RIESGOS

Los riesgos del proyecto se clasificarán según las áreas de gestión de proyectos descritas en la Guía PMBOK, lo que permitirá identificar y gestionar amenazas y oportunidades de forma estructurada y eficiente:

**1. Riesgos en la Gestión del Alcance del Proyecto:** Estos riesgos están relacionados con la posibilidad de cambios, malentendidos o falta de claridad en los requisitos y objetivos del proyecto. Los problemas en esta área pueden generar desviaciones significativas en el alcance, afectando el éxito final del proyecto.

**1. Riesgos en la Gestión del Cronograma del Proyecto:** Son riesgos que afectan los plazos de ejecución y las fechas de entrega del proyecto. Un mal control del cronograma puede causar retrasos que afecten todo el ciclo de vida del proyecto y comprometan los plazos comprometidos con los stakeholders.

**1. Riesgos en la Gestión de los Costes del Proyecto:** Estos riesgos impactan el presupuesto del proyecto, generando sobrecostos o la necesidad de financiamiento adicional no previsto. Un mal control de los costos puede llevar a la inviabilidad económica del proyecto.

**1. Riesgos en la Gestión de la Calidad del Proyecto:** Estos riesgos se relacionan con la capacidad del proyecto para cumplir con los estándares de calidad definidos en los entregables. Un fallo en la calidad puede llevar a la insatisfacción del cliente o la necesidad de reprocesos, aumentando los costos y tiempos del proyecto.

**1. Riesgos en la Gestión de Recursos Humanos:** Estos riesgos se relacionan con el equipo de trabajo, sus competencias, disponibilidad, y el clima laboral del proyecto. La falta de motivación o la falta de recursos humanos clave puede poner en riesgo el éxito del proyecto.

**1. Riesgos en la Gestión de Comunicaciones:** Estos riesgos están relacionados con la eficacia de la comunicación entre el equipo del proyecto, los stakeholders y otros interesados. La falta de una adecuada gestión de la información puede llevar a malentendidos o decisiones erróneas.

**1. Riesgos en la Gestión de las Adquisiciones:** Estos riesgos se derivan de la compra de bienes y servicios necesarios para completar el proyecto. Problemas en las adquisiciones pueden generar retrasos, sobrecostos o fallos en los materiales o servicios contratados.

**1. Riesgos en la Gestión de Stakeholders del Proyecto:** Estos riesgos se relacionan con la gestión de las expectativas y el involucramiento de las partes interesadas (stakeholders). Si los stakeholders no se gestionan adecuadamente, pueden influir negativamente en las decisiones del proyecto o incluso boicotear su progreso.

# 3\. METODOLOGÍA PARA RECOGIDA DE RIESGOS

Los riesgos de la organización serán recogidos en el documento de registro de riesgos. En este documento se elaborará una lista de los riesgos agrupados en distintas categorías y se deberá aportar la siguiente información de cada uno de ellos:

- **ID del riesgo:** deberá llevar el formato RXX-000 siendo XX siglas de la categoría de erro correspondiente que se especificará a continuación.
- **Nombre**: Un título breve y descriptivo que identifica el riesgo, como _Retraso en la entrega del proveedor_.
- **Descripción**: Un resumen detallado del riesgo, explicando su naturaleza, causas y posibles consecuencias, por ejemplo, _El proveedor clave podría retrasar la entrega de componentes críticos_.
- **Probabilidad**: Un porcentaje o calificación que indica la probabilidad de que ocurra el riesgo, como _Alta probabilidad del 70%_.
- **Impacto en el coste**: Evaluación del efecto que el riesgo tendría en el presupuesto del proyecto, como _Aumento de 10.000 € en los costes_.
- **Impacto en el alcance**: Cómo el riesgo podría afectar los entregables o el alcance del proyecto, por ejemplo, _El alcance del proyecto podría reducirse en un 15%_.
- **Impacto en el tiempo**: La repercusión que tendría el riesgo en el cronograma del proyecto, como _Retraso de dos semanas en la finalización_.
- **Impacto en la calidad**: Cómo el riesgo podría afectar la calidad de los entregables, por ejemplo, _Reducción de la calidad en los componentes finales debido a cambios de último minuto_.
- **Seguimiento y respuesta (evitar, transferir, mitigar o aceptar)**: Las acciones que se tomarán para monitorear el riesgo y mitigar su impacto, como _Se revisará semanalmente y se contactará al proveedor para obtener actualizaciones frecuentes_.

Además, los riesgos estarán clasificados en una de las siguientes categorías:

- RIESGOS EN LA GESTIÓN DEL ALCANCE (RAL-000)
- RIESGOS EN LA GESTIÓN DEL CRONOGRAMA (RCR-000)
- RIESGOS EN LA GESTIÓN DE LOS COSTES (RCO-000)
- RIESGOS EN LA GESTIÓN DE LA CALIDAD (RCA-000)
- RIESGOS EN LA GESTIÓN DE RECURSOS HUMANOS (RRH-000)
- RIESGOS EN LA GESTIÓN DE COMUNICACIONES (RCM-000)
- RIEGOS EN LA GESTIÓN DE LAS ADQUISICIONES (RAD-000)
- RIEGOS EN LA GESTIÓN DE STAKEHOLDERS (RST-000)

# 4\. METODOLOGÍA PARA ANÁLISIS Y PRIORIZACIÓN DE RIESGOS

### ANÁLISIS DE RIESGOS

Los riesgos identificados en primera instancia son los riesgos de alto nivel incluidos en el Acta de Constitución del proyecto. El resto de los riesgos partirán de los anteriormente mencionados y serán recogidos en el Registro de Riesgos. Una vez recogidos e inidentificados se procederá a un **análisis cuantitativo** de la siguiente manera:

- En primer lugar, se definirán **una escala de probabilidad de los riesgos** con cinco intervalos (muy alta, alta, media, baja, muy baja). Esta probabilidad se generalizará en los rangos 1, 3, 5, 7, 9 respectivamente a los intervalos antes mencionados.
- Se definirá una **escala de impacto de los riesgos** en factores a nivel de proyecto y producto como lo serán el **alcance, coste, tiempo y calidad**. Por cada factor se deberá estimar en una escala con cinco intervalos (similar a la de probabilidad) el efecto que puede tener un riesgo para cada uno de esos factores. Para la escala numérica de estas matrices se ha decicido promediar en cada factor, obteniendo así un valor distinto para cada factor en lugar de usar siempre la misma escala 1, 3, 5, 7, 9 para todos los factores. La idea es conseguir una matriz distinta para cada factor (alcance, coste, tiempo y calidad) ya que no tiene el mismo valor de riesgo un riesgo con impacto medio en el tiempo que en el alcance, ya que el tiempo se puede recuperar de alguna forma, mientras que el alcance es un factor mucho más crítico.
- Por último, se elaborará una **matriz de probabilidad-impacto** por cada uno de los factores para así poder visualizar a simple vista la importancia que debe tener cada riesgo en función del tiempo y coste que requieran y la forma en la que afecten al alcance del proyecto y a la calidad del producto. En esta matriz, cada celda tomará un **VALOR DE RIESGO**, producto del impacto y la probabilidad de ese riesgo.

\

#### DEFINICIONES DE PROBABILIDAD


\begin{table}[!ht]
\centering
\begin{tabular}{|>{\columncolor{green!20}}p{2cm}|>{\columncolor{cyan!20}}p{2cm}|>{\columncolor{yellow!20}}p{2cm}|>{\columncolor{orange!20}}p{2cm}|>{\columncolor{red!20}}p{2cm}|}
\hline
\textbf{Muy bajo 1} & \textbf{Bajo 3} & \textbf{Moderado 5} & \textbf{Alto 7} & \textbf{Muy Alto 9} \\
\hline
\rowcolor{white}
Casi imposible que ocurra & Poco probable que ocurra & Ocurre de vez en cuando & Ocurre con frecuencia & Casi seguro que ocurre \\
\hline
0\% < P $\leq$ 1\% & 1\% < P $\leq$ 10\% & 10\% < P $\leq$ 50\% & 50\% < P $\leq$ 80\% & 80\% < P $\leq$ 100\% \\
\hline
\end{tabular}
\end{table}

\

#### DEFINICIONES DE IMPACTO

\begin{table}[!ht]
\centering
\begin{tabular}{|p{2cm}|>{\columncolor{green!20}}p{2cm}|>{\columncolor{cyan!20}}p{2cm}|>{\columncolor{yellow!20}}p{2cm}|>{\columncolor{orange!20}}p{2cm}|>{\columncolor{red!20}}p{2cm}|}
\hline
\textbf{DIMENSIÓN} & \textbf{Muy bajo 1} & \textbf{Bajo 3} & \textbf{Moderado 5} & \textbf{Alto 7} & \textbf{Muy Alto 9} \\
\hline
\rowcolor{white}
\textbf{Alcance} & Afecta a menos del 5\% de los paquetes de trabajo. & Afecta entre el 5\% y el 10\% de los paquetes de trabajo. & Afecta entre el 10\% y el 20\% de los paquetes de trabajo. & Afecta entre el 20\% y el 30\% de los paquetes de trabajo. & Afecta a más del 30\% de los paquetes de trabajo. \\
\hline
\textbf{Tiempo} & No afecta a actividades de la cadena crítica. & Afecta a actividades de la cadena crítica, pero no extiende la duración del proyecto. & Extiende la duración del proyecto menos del 2\%. & Extiende la duración del proyecto menos del 5\%. & Extiende la duración del proyecto más del 5\%. \\
\hline
\rowcolor{white}
\textbf{Costes} & Aumenta los costes en menos del 1\%. & Aumenta los costes en menos del 3\%. & Aumenta los costes en menos del 5\%. & Aumenta los costes en menos del 7\%. & Aumenta los costes más del 7\%. \\
\hline
\end{tabular}
\end{table}


\newpage


### PRIORIZACIÓN DE RIESGOS

Según lo mencionado, la priorización de cada riesgo será determinada en función de su valor de riesgo. Este valor de riesgo será el producto del impacto y de la probabilidad del riesgo.

**VALOR DE RIESGO = PROBABILIDAD DEL RIESGO \* IMPACTO DEL RIESGO**

De esta forma, obtendremos cuatro matrices de probabilidad en las que podremos ver a simple vista el valor de riesgo para el alcance, coste, tiempo y calidad de ese riesgo dado su probabilidad y su impacto.


\\ 

#### MATRIZ PROBABILIDAD x IMPACTO COSTES

\begin{table}[!ht]
\centering
\begin{tabular}{|c|>{\columncolor{green!20}}c|>{\columncolor{cyan!20}}c|>{\columncolor{yellow!20}}c|>{\columncolor{orange!20}}c|>{\columncolor{red!20}}c|}
\hline
\textbf{PROBABILIDAD x COSTES} & \textbf{Muy bajo 1} & \textbf{Bajo 3} & \textbf{Medio 5} & \textbf{Alto 7} & \textbf{Muy Alto 9} \\
\hline
\rowcolor{white}
\textbf{Muy alto 0.52} & 0.52 & 1.56 & 2.6 & 3.64 & 4.68 \\
\hline
\textbf{Alto 0.4} & 0.4 & 1.2 & 2 & 2.8 & 3.6 \\
\hline
\rowcolor{white}
\textbf{Medio 0.25} & 0.25 & 0.75 & 1.25 & 1.75 & 2.25 \\
\hline
\textbf{Bajo 0.15} & 0.15 & 0.45 & 0.75 & 1.05 & 1.35 \\
\hline
\rowcolor{white}
\textbf{Muy bajo 0.05} & 0.05 & 0.15 & 0.25 & 0.35 & 0.45 \\
\hline
\end{tabular}
\end{table}

\\

#### MATRIZ PROBABILIDAD x IMPACTO CALIDAD

\begin{table}[!ht]
\centering
\begin{tabular}{|c|>{\columncolor{green!20}}c|>{\columncolor{cyan!20}}c|>{\columncolor{yellow!20}}c|>{\columncolor{orange!20}}c|>{\columncolor{red!20}}c|}
\hline
\textbf{PROBABILIDAD x CALIDAD} & \textbf{Muy bajo 1} & \textbf{Bajo 3} & \textbf{Medio 5} & \textbf{Alto 7} & \textbf{Muy Alto 9} \\
\hline
\rowcolor{white}
\textbf{Muy alto 0.5} & 0.5 & 1.5 & 2.5 & 3.5 & 4.5 \\
\hline
\textbf{Alto 0.1} & 0.1 & 0.3 & 0.5 & 0.7 & 0.9 \\
\hline
\rowcolor{white}
\textbf{Medio 0.05} & 0.05 & 0.15 & 0.25 & 0.35 & 0.45 \\
\hline
\textbf{Bajo 0.01} & 0.01 & 0.03 & 0.05 & 0.07 & 0.09 \\
\hline
\rowcolor{white}
\textbf{Muy bajo 0} & 0 & 0 & 0 & 0 & 0 \\
\hline
\end{tabular}
\end{table}

\\

#### MATRIZ PROBABILIDAD x IMPACTO ALCANCE

\begin{table}[!ht]
\centering
\begin{tabular}{|c|>{\columncolor{green!20}}c|>{\columncolor{cyan!20}}c|>{\columncolor{yellow!20}}c|>{\columncolor{orange!20}}c|>{\columncolor{red!20}}c|}
\hline
\textbf{PROBABILIDAD x ALCANCE} & \textbf{Muy bajo 1} & \textbf{Bajo 3} & \textbf{Medio 5} & \textbf{Alto 7} & \textbf{Muy Alto 9} \\
\hline
\textbf{Muy alto 0.65} & 0.65 & 1.95 & 3.25 & 4.55 & 5.85 \\
\hline
\rowcolor{white}
\textbf{Alto 0.25} & 0.25 & 0.75 & 1.25 & 1.75 & 2.25 \\
\hline
\textbf{Medio 0.15} & 0.15 & 0.45 & 0.75 & 1.05 & 1.35 \\
\hline
\rowcolor{white}
\textbf{Bajo 0.075} & 0.075 & 0.225 & 0.375 & 0.525 & 0.675 \\
\hline
\textbf{Muy bajo 0.025} & 0.025 & 0.075 & 0.125 & 0.175 & 0.225 \\
\hline
\rowcolor{white}
\textbf{Muy alto 0.65} & 0.65 & 1.95 & 3.25 & 4.55 & 5.85 \\
\hline
\end{tabular}
\end{table}

\\ 

#### MATRIZ PROBABILIDAD x IMPACTO TIEMPO

\begin{table}[!ht]
\centering
\begin{tabular}{|c|>{\columncolor{green!20}}c|>{\columncolor{cyan!20}}c|>{\columncolor{yellow!20}}c|>{\columncolor{orange!20}}c|>{\columncolor{red!20}}c|}
\hline
\textbf{PROBABILIDAD x TIEMPO} & \textbf{Muy bajo 1} & \textbf{Bajo 3} & \textbf{Medio 5} & \textbf{Alto 7} & \textbf{Muy Alto 9} \\
\hline
\textbf{Muy alto 0.525} & 0.525 & 1.575 & 2.625 & 3.675 & 4.725 \\
\hline
\rowcolor{white}
\textbf{Alto 0.25} & 0.25 & 0.75 & 1.25 & 1.75 & 2.25 \\
\hline
\textbf{Medio 0.1} & 0.1 & 0.3 & 0.5 & 0.7 & 0.9 \\
\hline
\rowcolor{white}
\textbf{Bajo 0.05} & 0.05 & 0.15 & 0.25 & 0.35 & 0.45 \\
\hline
\textbf{Muy bajo 0} & 0 & 0 & 0 & 0 & 0 \\
\hline
\end{tabular}
\end{table}


\newpage


# 5\. RESERVAS DE CONTINGENCIA

Cuando el equipo de dirección del proyecto lo considere necesario, se podrá hacer uso de la reserva de contingencia para implementar los planes de respuesta a los riesgos identificados en el acta de constitución del proyecto. Esto incluye tanto los planes de contingencia como los planes de respaldo, en caso de que los primeros no resulten efectivos.

**Se considerará necesario el uso de las reservas de contingencia solo cuando la situación supere un valor de riesgo superior a 4 en su matriz de alcance correspondiente.**

# 6\. PROTOCOLOS PARA CONTINGENCIAS

En caso de que un riesgo se materialice, se seguirán los siguientes protocolos:

- Activación del plan de contingencia: El jefe de equipo y el director del proyecto ejecutarán el plan de contingencia definido para el riesgo en cuestión.
- Registro de la incidencia: Se actualizará el registro de riesgos con el estado actual y las medidas tomadas.
- Revisión y actualización: El plan de riesgos será revisado para analizar si es necesario actualizar las medidas de contingencia o identificar nuevos riesgos relacionados.

# 7\. ACTIVIDADES DE SEGUIMIENTO DE RIESGOS

Las actividades de seguimiento se llevarán a cabo de forma continua y a lo largo de todo el proyecto. Estas incluyen:

- Monitoreo de riesgos: Revisión constante del estado de los riesgos y su evolución en el Registro de Riesgos
- Evaluación de nuevas amenazas: Identificación y análisis de nuevos riesgos durante las reuniones de seguimiento.
- Revisión de los planes de contingencia: Validación y ajustes en los planes de contingencia según el estado actual del proyecto.

# 8\. INFORMES DE SEGUIMIENTO DE RIESGOS

A lo largo del proyecto, los riesgos identificados deben ser monitoreados de forma regular. Además, es necesario verificar si las acciones de mitigación están siendo implementadas y si son eficaces. En caso de que ocurra un riesgo, se debe asegurar que se ejecute el Plan de Contingencia previsto.

- Plan de riesgos: Documento formal que describe el proceso de gestión de riesgos del proyecto y su seguimiento.
- Registro de riesgos: Documento que incluye los riesgos identificados, su descripción, causas, tipos y categorías. Se actualizará continuamente durante todo el proyecto y será la base para el seguimiento de los riesgos.
- Actualizaciones del plan del proyecto: Como resultado del proceso de gestión de riesgos, se actualizará el plan del proyecto para reflejar los ajustes necesarios.
- Solicitudes de cambio: La gestión de riesgos puede generar propuestas de cambios en diferentes aspectos del proyecto, que serán documentadas y presentadas al cliente para su evaluación en el comité correspondiente, donde se decidirá si se implementan.
- Registro de cambios: Documento donde se agrupan las medidas correctivas y preventivas propuestas para abordar los riesgos identificados.

# 9\. ROLES Y RESPONSABLES

El **responsable de Riesgos** tendrá la tarea de supervisar y controlar las actividades clave del proyecto para anticiparse a posibles desviaciones en comparación con la planificación original, y proponer soluciones considerando el impacto en el alcance, el tiempo y el coste. Las responsabilidades del responsable de Riesgos del Proyecto incluirán:

- Mantener actualizadas las matrices de riesgos si se producen nuevas estimaciones o nuevos riesgos o incidencias que hagan variar la probabilidad de algunos de los factores.
- Si se identifica un nuevo riesgo que sea clasificado como alto o severo, se informará de inmediato al Project Manager, y si es necesario, el equipo se reunirá de urgencia para evaluar y tomar decisiones al respecto.

Por otra parte, el **equipo de desarrollo**:

- Deberá gestionar los riesgos identificados, mitigaciones aplicadas o controles implementados, con el fin de mantener la gestión de riesgos siempre actualizada. Esto aplica independientemente del nivel de riesgo, aunque **se debe priorizar la mitigación de los riesgos más severos**.
- Informar al responsable de Riesgos y al jefe de proyecto sobre nuevos riesgos detectado.

Por último, cabe mencionar cuales serían los **interesados** en la identificación y resolución de cada uno de los riesgos:

En general, el interesado principal en la gestión de riesgos referentes al producto es el **Product Owner**, ya que este tiene como objetivo que el producto cumpla con sus necesidades limitándose en coste y tiempo. Por extensión, estos riesgos también conciernen al jefe de proyecto y al equipo de desarrollo ya que un cliente no satisfecho implica una mala ejecución del trabajo realizado.

Por otro lado, los requisitos más relacionados con una gestión a nivel de proyecto conciernen al **equipo de trabajo** y principalmente al **jefe de proyecto** más que al cliente. Estos pueden ser riesgos en la gestión de las comunicaciones, en la gestión de adquisiciones o riesgos en los recursos humanos ya que estos son asuntos que no afectan de manera directa al producto, pero si a la gestión de la organización.
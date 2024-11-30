---
title: "Plan de Gestión de los Recursos"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "04/11/2024"  # modificar
subject: "PGPI"
author: [Daniel Fernández Caballero, Ramón Gavira Sánchez, José Miguel Iborra Conejo, Antonio Macías Ferrera, Rafael Pulido Cifuentes]
lang: "es"
titlepage: true,
titlepage-text-color: "1C1C1C"
titlepage-rule-color: "1C1C1C"
titlepage-rule-height: 0
titlepage-background: "../../../plantilla-markdown/background2V.pdf" # modificar si el doc es horizontal
footer-left: "Pueblista - PGPI"
footer-right: "\\thepage"
toc: true
toc-own-page: true
documentclass: scrartcl
classoption: "table"        
header-includes:        # para los colores en las tablas
    - \usepackage{float}
---

**PLAN DE GESTIÓN DE LOS RECURSOS**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces
- **CÓDIGO DEL PROYECTO:** 2.15
- **FECHA DE CREACIÓN:** 26/10/2024
- **VERSIÓN DEL DOCUMENTO:** 1.2
 \newline 

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO**

|Fecha	|Realizada por	|Breve descripción de los cambios
| ----- | ------------- | ----------------- |
| 26/10/2024	|  Daniel Fernández Caballero, Antonio Macías Ferrera	| Elaboración del documento.   |
| 04/11/2024	| Antonio Macías Ferrera	| Corrección de errores de formato.   |

\newpage



# 1\. NORMAS Y PROCEDIMIENTOS APLICABLES 
Este Plan de Gestión de los Recursos seguirá de manera estricta los procedimientos, metodologías y mejores prácticas establecidos en la **Guía del PMBOK** (Project Management Body of Knowledge), publicada por el Project Management Institute (PMI).

Para una correcta gestión de los recursos: primero se deberá establecer una correcta identificación de los recursos; una correcta definición de roles y responsabilidades, lo que irá acompañado de una matriz de responsabilidades; un correcto plan de gestión de los recursos de acuerdo con la EDT y el cronograma, y una política de contrataciones y formación estipulada si procede. 


# 2\. CUMPLIMIENTO DE ESTÁNDARES Y REGLAMENTACIONES 
### Recursos Humanos 
Los recursos humanos (RRHH), estarán conformados por el **personal que se encargará de llevar a cabo el proyecto** o intervenir en él en mayor o menor medida. De entre ellos, los participantes explícitos del proyecto tendrán asignados un rol y una serie de responsabilidades. Estos recursos humanos se dividen a su vez en dos equipos: **equipo de dirección y equipo de ejecución**. 

### Recursos Materiales 
Dentro de un proyecto software, determinamos como recursos materiales a todos aquellos **recursos no humanos, que no tiene por qué ser físicos**. Con estos, entran dentro de esta definición las licencias software, programas, suscripciones, equipos y otros materiales que son necesarios de manera directa o indirecta para que el proyecto se lleve a cabo. 

### Roles y responsabilidades
Cada equipo de trabajo o miembro individual del proyecto deberá acometer uno o varios roles dentro de este. Cada rol llevará asociadas una serie de responsabilidades en relación con la ejecución del proyecto y la elaboración del producto. 

Se debe realizar una trazabilidad de los roles respecto a las tareas de la EDT en las que deben trabajar. Para ello, se cuenta con una **matriz de asignación de responsabilidades** en la que, por cada tarea de la EDT de cada uno de los paquetes, se designará un rol **Responsable**, **Consultado**, **Aprobador** e **Informado** al respecto. 


\newpage


# 3\. RECURSOS HUMANOS 

### Equipo de Dirección

|**ROL**|**RESPONSABILIDADES**|**HABILIDADES**|
| - | - | - |
|*Director de Proyecto*| - Crear el Acta de Constitución, el Plan de Dirección del Proyecto, y los planes de cronograma y presupuesto. \newline - Supervisar la ejecución del proyecto, asegurando que se cumplan los objetivos de tiempo, costo y calidad. \newline - Facilitar reuniones periódicas con stakeholders y comunicar los avances clave. \newline - Monitorear y ajustar los planes del proyecto según sea necesario. \newline - Gestionar los recursos del proyecto, tanto humanos como financieros.| \newline - Liderazgo y toma de decisiones. \newline - Habilidad de planificación y organización. \newline - Comunicación efectiva y resolución de conflictos. \newline - Conocimiento de herramientas de gestión de proyectos (MS Project, herramientas ágiles, etc).|
|*Analista-técnico*| - Recopilar y analizar los requisitos del sistema, asegurando que sean claros y alcanzables. \newline - Documentar los requisitos y especificaciones del sistema, junto con el alcance de este. \newline - Elaborar la documentación de la fase de planificación. \newline - Colaborar con el <a name="_int_ultvliff"></a>Director de Proyecto para asegurar que los entregables cumplan con las expectativas. \newline - Apoyar en la identificación de riesgos y supuestos asociados a los requisitos.| - Análisis de sistemas y documentación de requisitos. \newline - Comunicación y negociación con stakeholders. \newline - Pensamiento crítico y atención al detalle. \newline - Conocimiento en metodologías de análisis y modelado de sistemas. \newline - Conocimiento en negocios y dominios de tecnología. \newline - Habilidad de absorber y entender rápidamente cualquier información.|
|*Responsable gestión de la comunicación e información*| - Crear el Plan de Gestión de las Comunicaciones y asegurarse de que todos los miembros del proyecto están bien informados. \newline - Establecer y mantener canales de comunicación efectivos entre todos los stakeholders. \newline - Monitorear y documentar el flujo de información, asegurando su correcta distribución.|-  Comunicación y habilidades interpersonales. \newline - Organización y habilidad para gestionar la información de manera estructurada. \newline - Conocimiento en herramientas de comunicación (Slack, Teams, etc.). \newline - Habilidad para crear reportes de estado de manera clara y precisa.|
|*Responsable de aseguramiento de la calidad*| \newline - Desarrollar y mantener el Plan de Gestión de Calidad, asegurando que se cumplan los estándares de calidad definidos. \newline - Realizar auditorías de calidad periódicas para evaluar el cumplimiento de los requisitos de calidad. \newline - Monitorear y validar los entregables para asegurar que cumplan con los estándares de calidad. \newline - Colaborar con el equipo de desarrollo para implementar mejoras en los procesos.| \newline - Conocimiento en estándares de calidad y accesibilidad (ISO, CMMI, WCAG 2.1). \newline - Habilidad para realizar auditorías y evaluaciones de calidad. \newline - Orientación a los detalles y habilidades de documentación. \newline - Capacidad de análisis y mejora de procesos.|
|*Responsable de Gestión de riesgos*| - Identificar, evaluar y documentar los riesgos del proyecto en el Registro de Riesgos. \newline - Monitorear los riesgos y ejecutar los planes de respuesta para mitigar impactos negativos. \newline - Realizar revisiones periódicas del estado de los riesgos y actualizar las estrategias de mitigación. \newline - Comunicar los riesgos y sus posibles impactos al Director de Proyecto y otros stakeholders relevantes.| - Habilidad para identificar y evaluar riesgos. \newline - Capacidad de planificación y desarrollo de estrategias de mitigación. \newline - Conocimiento en metodologías de gestión de riesgos (PMI, ISO 31000). \newline - Comunicación efectiva para informar sobre riesgos y su evolución.|


\newpage


## Equipo de Desarrollo

|**ROL**|**RESPONSABILIDADES**|**HABILIDADES**|
| - | - | - |
|*Analista-programador*| - Recopilar y analizar los requisitos del sistema, asegurando que sean claros y alcanzables. \newline - Documentar los requisitos y especificaciones del sistema, junto con el alcance de este. \newline - Elaborar la documentación de la fase de planificación. \newline - Facilitar la comunicación de requerimientos entre stakeholders y el equipo de desarrollo. \newline - Colaborar con el Director de Proyecto para asegurar que los entregables cumplan con las expectativas.|- Análisis de sistemas y documentación de requisitos. \newline - Comunicación y negociación con stakeholders. \newline - Pensamiento crítico y atención al detalle. \newline - Conocimiento en metodologías de análisis y modelado de sistemas. \newline - Conocimiento en negocios y dominios de tecnología. \newline - Habilidad de absorber y entender rápidamente cualquier información.|
|*Programador*| - Desarrollar el código del sistema conforme a los requisitos técnicos y funcionales. \newline - Documentar el código para facilitar su mantenimiento y futuras mejoras. \newline - Realizar pruebas unitarias y de integración para verificar el funcionamiento del sistema. \newline - Colaborar con el Analista para resolver dudas técnicas y cumplir con los requisitos. \newline - Optimizar el rendimiento del código y seguir estándares de calidad.| - Dominio de programación en el stack tecnológico del proyecto (Python, Django). \newline - Experiencia en pruebas unitarias e integradas. \newline - Conocimiento de buenas prácticas de desarrollo (Clean Code). \newline - Capacidad para resolver problemas técnicos de manera eficiente.|
|*Tester*| - Diseñar y ejecutar casos de prueba para evaluar la funcionalidad y rendimiento del sistema. \newline - Documentar y reportar errores, colaborando con el equipo de desarrollo para solucionarlos. \newline - Realizar pruebas de regresión para asegurar la estabilidad del sistema tras cada cambio. \newline - Asegurar que el producto final cumpla con los requisitos de funcionalidad y calidad definidos.| - Conocimiento en técnicas y herramientas de pruebas (como Selenium, JUnit). \newline - Capacidad para diseñar casos de prueba y scripts de pruebas automatizadas. \newline - Orientación al detalle y habilidades analíticas. \newline - Capacidad de comunicación para documentar y explicar errores.|
|*Diseñador de UI/UX*| - Diseñar la interfaz de usuario enfocándose en la usabilidad y experiencia de usuario. \newline - Crear prototipos y wireframes. \newline - Colaborar con el equipo de desarrollo para implementar las interfaces. \newline - Iterar y mejorar el diseño según feedback de usuarios y pruebas de usabilidad.| - Diseño de interfaces de usuario y experiencia de usuario (UI/UX). \newline - Habilidad en herramientas de diseño (Bootstrap Studio). \newline - Conocimientos básicos en frontend para facilitar la implementación.|
|*Formador*| - Crear materiales de aprendizaje específicos y concisos, enfocados en competencias clave. \newline - Facilitar las sesiones de capacitación y adaptar el estilo de enseñanza según las necesidades del equipo. \newline - Proporcionar apoyo continuo para la aplicación práctica de los conocimientos en el proyecto. \newline - Evaluar el aprendizaje adquirido y recoger feedback para mejorar futuras formaciones.| - Capacidad para transmitir conceptos de manera clara y comprensible, adaptando el tono y el contenido al nivel de conocimiento del equipo. \newline - Dominio de las herramientas, metodologías y competencias clave que el equipo necesita para el proyecto. \newline - Habilidad para estructurar la formación en función del cronograma, asegurando el cumplimiento de objetivos en el tiempo establecido. \newline - Competencia en evaluar el aprendizaje y aplicar mejoras en el proceso formativo basadas en feedback y resultados observados.|
|*Experto en accesibilidad*| - Revisar y garantizar que el producto cumpla con los estándares de accesibilidad AA de la Junta de Andalucía en todas las fases del proyecto. \newline - Brindar asesoramiento sobre prácticas de diseño accesible y ajustar la implementación para que cumpla con los criterios AA. \newline - Realizar pruebas exhaustivas para detectar y corregir barreras de accesibilidad en el diseño y funcionalidad.| - Conocimiento en Normativa de Accesibilidad, especialmente en las normas AA de la Junta de Andalucía y WCAG 2.1. \newline - Habilidad para identificar, analizar y resolver problemas de accesibilidad en la interfaz. \newline - Capacidad para explicar requisitos técnicos y conceptos de accesibilidad al equipo no especializado de forma clara. \newline - Estar enfocado en crear una experiencia inclusiva para todos los usuarios, asegurando que el producto final sea fácil de usar y accesible.|



# 4\. CALENDARIO DE RECURSOS HUMANOS 
## 4\.1 POLÍTICAS DE RECURSOS HUMANOS Y DISPONIILIDAD DEL EQUIPO

La empresa aplicará las siguientes políticas de recursos humanos para la organización del proyecto. Este enfoque responde a las exigencias de entregas y márgenes establecidos en el *Plan de Gestión del Cronograma.*

- **Jornada Laboral:**
  - **De lunes a domingo,** todos los días, estarán asignados como laborables para cumplir con los objetivos del proyecto.
  - La jornada laboral acumulada será de 40 horas semanales, respetando la normativa vigente.
  - Habrá flexibilidad en el número de horas diarias trabajadas; en algunos días se podrá extender la jornada del proyecto, mientras que en otros el equipo podrá tomar horas libres para asegurar el equilibrio de las 40 horas. Además, cada persona, mantendrá una tarde libre fija a la semana, previamente notificada al equipo del proyecto.
- **Guardias y disponibilidad en festivos:**
  - En función de las necesidades del proyecto, podrán solicitarse guardias para fines de semana o días festivos específicos.
  - La programación de estas guardias será previa y consensuada con los miembros del equipo, respetando la normativa vigente en cuanto a remuneración y descansos compensatorios.
  - En caso de requerirse trabajo en un festivo, el equipo recibirá aviso con suficiente antelación, y la empresa compensará este tiempo mediante pago adicional o días libres según el convenio correspondiente.
- **Modalidad de Trabajo:** Aunque se fomenta el teletrabajo, las instalaciones están disponibles para aquellos que deseen combinar esta modalidad con la presencialidad.
- **Reuniones de seguimiento del proyecto:** 
  - Se realizarán dos reuniones semanales: **lunes a las 16:00 y miércoles a las 18:30.** La asistencia es obligatoria, salvo circunstancias excepcionales.
- **Vacaciones y Festivos:**
  - Cada miembro del equipo cuenta con **20 días laborables de vacaciones** anuales, respetándose el calendario de festivos nacionales y los correspondientes a Andalucía y Sevilla. Las vacaciones deberán planificarse para no interferir en los períodos críticos del proyecto y se coordinarán anticipadamente.

## 4\.2. DISPONIBILIDAD Y DEDICACIÓN DEL EQUIPO

Cada miembro del equipo estará disponible **al 100% para la empresa** durante el horario laboral general. Sin embargo, se establece que la dedicación directa a este proyecto será ajustada según la fase y naturaleza de las actividades, con un **porcentaje de dedicación variable** que se registrará en el desglose de costos y el cronograma en MS Project.

Dado que se entiende que los integrantes no estarán al 100% activos en cada momento, se asumirá un **factor de improductividad del 15%** en la dedicación, que afectará a los costes. Esto permitirá una estimación realista del tiempo efectivo, considerando pausas necesarias, ajustes de ritmo y momentos de menor rendimiento, especialmente en fases de alta intensidad


\newpage


# 5\. PLAN DE FORMACIÓN 

El proyecto contempla un período de formación interna, ya que la formación a los usuarios finales queda excluida del alcance. No obstante, al equipo de la organización se le ofrecerá una formación que aborde tanto competencias técnicas como habilidades blandas, de modo que se prepare adecuadamente para la ejecución eficiente y efectiva del proyecto.

## Objetivos de la Formación
- **Mejorar las Competencias Técnicas**: Asegurar que todos los miembros del equipo dominen las herramientas y tecnologías necesarias para el desarrollo del proyecto.
- **Desarrollar Habilidades Blandas**: Fomentar la comunicación efectiva, trabajo en equipo y liderazgo.
- **Preparación para Entregas Rápidas**: Asegurar que el equipo esté preparado para realizar entregas continuas y de alta calidad.

## Identificación de Necesidades
- **Análisis de Competencias**: Realizar una evaluación inicial de las habilidades del equipo para identificar áreas de mejora.
- **Reunión de Kick-off**: Discutir las necesidades formativas específicas durante la reunión inicial.

## Contenidos de la Formación
- **Formación Técnica**:
  - **Lenguajes de Programación**: Capacitación en Python y Django.
  - **Herramientas de Gestión**: Formación en MS Project y metodologías ágiles.
  - **Pruebas y Calidad**: Talleres sobre técnicas de pruebas y estándares de calidad.
- **Formación en Habilidades Blandas**:
  - **Comunicación Efectiva**: Cursos sobre técnicas de presentación y negociación.
  - **Trabajo en Equipo**: Actividades para fortalecer la colaboración y cohesión del grupo.
  - **Liderazgo**: Talleres para el desarrollo de habilidades de liderazgo y gestión de conflictos.

## Metodología
- **Sesiones Presenciales y Virtuales**: Alternar entre cursos en línea y talleres presenciales para maximizar la accesibilidad.
- **Proyectos Prácticos**: Integrar ejercicios prácticos relacionados con el trabajo real del equipo para aplicar los conocimientos adquiridos.
- **Mentoría**: Asignar mentores para guiar a los miembros del equipo menos experimentados.


## Calendario de Formación
Para este proyecto, debido a su corta duración y magnitud, el plan de formación será de un mes siguiendo el siguiente esquema: 

- **Semana 1**:
  - Día 1: Evaluación inicial y talleres de formación técnica.
  - Día 2-3: Talleres de habilidades blandas.
  - Día 4-5: Ejercicios prácticos y sesiones de revisión.
- **Semana 2**:
  - Formación técnica continua y seguimiento de implementación.
- **Semanas 3-4**:
  - Aplicación práctica de conocimientos y revisión semanal de progreso.

## Evaluación de Resultados
- **Feedback de los Participantes**: Encuestas post-formación para medir la satisfacción y aplicabilidad de lo aprendido.
- **Medición de Impacto**: Comparar el rendimiento del equipo antes y después de la formación a través de indicadores clave de rendimiento (KPI).
- **Ajustes Necesarios**: Revisión del plan de formación y ajustes según las necesidades identificadas en las evaluaciones.

## Presupuesto
- **Costos de Formación**: Incluir honorarios de formadores, materiales y recursos necesarios.
- **Inversión en Herramientas**: Presupuestar licencias para plataformas de formación y herramientas de gestión.


\newpage


# 6\. PLAN DE RECONOCIMIENTO Y RECOMPENSA
Fomentar el desarrollo del equipo de proyecto contribuye a fortalecer tanto las habilidades individuales de sus miembros como la colaboración entre ellos, con el propósito de optimizar el trabajo en conjunto y mejorar el rendimiento general del proyecto. Para llevar a cabo esta dinámica se ha planteado un sistema que en lugar de fomentar la competitividad individual fomenta la autoevaluación y el autorreconocimiento. 

En concreto, usaremos una dinámica llamada “**Calendarios Niko Niko**” que se empezará a realizar cuando comience la fase de ejecución del proyecto y consistirá en un calendario diario en el que cada miembro del equipo deberá evaluar y describir su estado de ánimo en los días de trabajo con respecto al proyecto. Tras cada reunión semanal, se evaluará la moral del grupo y se tomarán medidas de forma conjunta e individual para conseguir mejorar el trabajo del equipo si fuera necesario. Para facilitar la descripción del estado de ánimo se usarán una serie de “emojis” en escala de los más negativos a los más positivos. A continuación, se muestra un ejemplo: 


\begin{figure}[H]
\centering
\includegraphics[width=0.4\textwidth]{../../img/ejemplo_niko_niko.png}
\caption{Ejemplo de uso de un calendario Niko-Niko}
\end{figure}


Algunos de los puntos positivos de esta dinámica son:

1. **Detección temprana de problemas**: El calendario Niko-Niko permite a los gestores de proyecto detectar cambios en el ánimo. Esto puede alertar sobre posibles problemas y tensiones, o contribuir a la detección temprana de problemas.
1. **Mejora la comunicación y la empatía**: Facilita un espacio seguro para expresar cómo se siente cada miembro del equipo, fomentando la empatía y abriendo la posibilidad de abordar problemas interpersonales o dificultades individuales de manera oportuna.
1. **Fomento de la autoevaluación y la autoconciencia**: Los miembros del equipo reflexionan diariamente sobre su estado de ánimo, lo cual les ayuda a ser más conscientes de su propio bienestar y las circunstancias que afectan su rendimiento.
1. **Mejora del clima laboral**: Un calendario Niko-Niko crea un ambiente de transparencia, mostrando que el bienestar del equipo es una prioridad para la organización. Esto puede mejorar la moral y la motivación del equipo, generando un entorno laboral más positivo.


\newpage


# 7\. RECURSOS MATERIALES
Como se ha mencionado anteriormente en el punto 2. , dentro de los recursos materiales, se encontrarán tanto recursos físicos (hardware), como lo son los equipos de trabajo o los periféricos, así como software necesario para el desarrollo del producto, tales como licencias, aplicaciones, servicios en la nube o entornos de desarrollo.

|**SOFTWARE**|**CANTIDAD**|**DESCRIPCIÓN**|
| - | - | - |
|VISUAL STUDIO CODE|5|Editor de código fuente altamente popular, ligero y extensible, que soporta múltiples lenguajes de programación y cuenta con una amplia variedad de extensiones para mejorar la productividad.|
|GIT|5|Sistema de control de versiones distribuido, utilizado para gestionar y realizar seguimiento de los cambios en proyectos de desarrollo de software.|
|GITHUB|5|Plataforma de alojamiento de repositorios de código, basada en Git, que facilita la colaboración en proyectos, la gestión de versiones y el seguimiento de problemas.|
|CHATGPT 4|1|Modelo avanzado de inteligencia artificial que proporciona asistencia mediante respuestas precisas y detalladas en múltiples contextos, útil para generar contenido y resolver dudas técnicas.|
|COPILOT |3|Herramienta de asistencia de programación basada en IA, integrada en editores como Visual Studio Code, que sugiere fragmentos de código en tiempo real para mejorar la productividad del desarrollador.|
|PANDOC|5|Convertidor de documentos universal que permite transformar archivos de texto en diferentes formatos, como Markdown, HTML, PDF, entre otros.|
|CLOCKIFY|5|Aplicación de seguimiento de tiempo que permite monitorizar la duración de tareas y proyectos, ideal para la gestión del tiempo y la facturación en entornos de trabajo.|
|MS OFFICE SUITE|5|Conjunto de aplicaciones de productividad de Microsoft que incluye Word, Excel, PowerPoint y otros, esenciales para la creación y gestión de documentos, hojas de cálculo y presentaciones.|
|MS PROJECT|2|Herramienta de gestión de proyectos de Microsoft, que permite planificar, asignar recursos, realizar seguimiento y controlar proyectos complejos de manera eficiente.|


\newpage


# 8\. CALENDARIO DE RECURSOS FÍSICOS

|**RECURSO**|**CANTIDAD**|**FECHA DE INICIO DE USO**|**FECHA DE FIN DE USO**|**RESPONSABLE**|
| :- | :- | :- | :- | :- |
|MACBOOK PRO 2020 M1|1|2/10/2024|6/12/2024|Equipo de Desarrollo, Equipo de Dirección|
|MACBOOK PRO 2019 i5|1|2/10/2024|6/12/2024|Equipo de Desarrollo, Equipo de Dirección|
|MSI MODERN 14 B11SB|3|2/10/2024|6/12/2024|Equipo de Desarrollo, Equipo de Dirección|
|RATÓN|5|2/10/2024|6/12/2024|Equipo de Desarrollo, Equipo de Dirección|
|TECLADO|5|2/10/2024|6/12/2024|Equipo de Desarrollo, Equipo de Dirección|
|CASCOS INALÁMBRICOS|5|2/10/2024|6/12/2024|Equipo de Desarrollo, Equipo de Dirección|
|VISUAL STUDIO CODE|5|7/11/2024|27/11/2024|Equipo de Desarrollo|
|GIT|5|2/10/2024|6/12/2024|Equipo de Desarrollo, Equipo de Dirección|
|GITHUB|5|2/10/2024|6/12/2024|Equipo de Desarrollo, Equipo de Dirección|
|CHATGPT 4|1|2/10/2024|6/12/2024|Equipo de Desarrollo, Equipo de Dirección|
|COPILOT |3|7/11/2024|27/11/2024|Equipo de Desarrollo|
|PANDOC|5| 2/10/2024|28/11/2024| 6/11/2024  6/12/2024| Equipo de Dirección|
|CLOCKIFY|5|2/10/2024|6/12/2024|Equipo de Desarrollo, Equipo de Dirección|
|MS OFFICE SUITE|5|  2/10/2024|28/11/2024 | 6/11/2024   6/12/2024|Equipo de Dirección|
|MS PROJECT|5|2/10/2024|6/12/2024|Equipo de Dirección|


\newpage


# ANEXO: ESTRUCTURA DE DESGLOSE DE LOS RECURSOS \newline

\begin{figure}[H]
\centering
\includegraphics[width=1.0\textwidth]{../../img/estructura_desglose_recursos.png}
\caption{Imagen estructura de desglose de los recursos}
\end{figure}

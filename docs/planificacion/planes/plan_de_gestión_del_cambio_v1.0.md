---
title: "Plan de gestión del cambio"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "27/10/2024"  # modificar
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
---

# PLAN DE GESTIÓN DEL CAMBIO

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces
- **CÓDIGO DEL PROYECTO:** 2.15
- **FECHA DE CREACIÓN:** 27/10/2024
- **VERSIÓN DEL DOCUMENTO:** 1.0

<br>

<br>

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO**

|Fecha	|Realizada por	|Breve descripción de los cambios
| ----- | ------------- | ----------------- |
| 25/10/2024	|  Rafael Pulido Cifuentes	| Elaboración del documento  |

\newpage


**PLAN DE GESTIÓN DEL CAMBIO**

# 1\. OBJETIVOS

Una gestión adecuada de los cambios es fundamental para orientar cualquier proyecto hacia el éxito. Dado que los cambios pueden surgir en cualquier momento a lo largo del ciclo de vida del proyecto, y considerando la incertidumbre inherente en la industria del software y la frecuencia de modificaciones en proyectos de corta duración como este, es crucial contar con un proceso sólido para su manejo.

Esto implica no solo gestionar los cambios internos que optimicen rendimiento, costos, plazos o productividad, sino también atender de forma rigurosa las solicitudes externas del cliente, evaluando y aprobando aquellas que aporten valor al proyecto y supervisando su implementación de manera efectiva.

## 2\. TIPOS DE CAMBIOS

Atendiendo al tipo de cambio, la gestión será de la siguiente forma: 

- **Cambios internos propuestos por un miembro del equipo**: Estos cambios serán comunicados al Director de Proyecto del equipo de desarrollo correspondiente. El equipo evaluará si la propuesta aporta beneficios sustanciales. Si es así, se registrará en el listado de control de cambios, incluyendo una descripción de las mejoras previstas con el cambio propuesto.
- **Cambios externos solicitados por el cliente**: Las solicitudes de cambio provenientes del cliente se documentarán en el listado de solicitudes de cambio, donde se analizará su impacto en el tiempo, los costos y el alcance establecidos en el proyecto. Además, se evaluará si afectan la calidad, los recursos asignados al proyecto y las adquisiciones necesarias.
- **Cambios relacionados con la gestión de la configuración del proyecto**: Estos cambios deben describirse en detalle. Se consideran modificaciones de configuración aquellas que afectan la estructura organizativa del proyecto, como ajustes en la estructura de carpetas, cambios en las nomenclaturas, creación de documentos nuevos o la adopción de una plantilla distinta.

## 3\. METODOLOGÍA Y FASES

Según ITIL, un cambio implica la adición, modificación o eliminación de cualquier elemento que pueda influir en los servicios, ya sea para resolver problemas detectados o en la búsqueda continua de mejoras en los servicios TIC. El procedimiento para gestionar una solicitud de cambio sigue un flujo estructurado de seis etapas consecutivas:

1. **Evaluación:** Se evalúa el riesgo y el impacto potencial del cambio en los servicios, considerando factores como la criticidad del cambio y los recursos necesarios para su implementación.
    - **Cambios dentro del alcance**: Si los cambios no afectan las líneas base del proyecto o, aunque tengan un impacto sustancial, aún se mantienen dentro de los límites de tiempo y costos autorizados, el Director del proyecto tendrá la autoridad para aprobar o rechazar dichos cambios.
    - **Cambios fuera de los límites definidos**: En el caso de que el impacto del cambio supere los límites definidos, la solicitud será escalada al Patrocinador del proyecto, quien tomará la decisión correspondiente.
2. **Clasificación:** Se realiza sobre los cambios dentro del alcance. Se clasifica el cambio de acuerdo con su tiempo de ejecución y urgencia.
    - **Cambios usuales**: Son cambios que se pueden darse regularmente con un riesgo bajo y bien controlado. Estos cambios están preaprobados y, por lo tanto, no necesitan pasar por el ciclo de aprobación.
    - **Cambios estándar**: Requieren una evaluación de riesgos y una aprobación explícita debido a su impacto potencial. No obstante, su ejecución no es urgente y, generalmente, se programan dentro de ventanas de mantenimiento. Ejemplos comunes de este tipo de cambio incluyen el despliegue de actualizaciones o parches y ajustes en configuraciones.
    - **Cambios urgentes**: Se trata de cambios que deben implementarse de inmediato debido al alto impacto que podrían tener en el servicio. Estos cambios siguen un flujo rápido de aprobación y suelen ser necesarios para resolver incidentes críticos que afectan la disponibilidad del servicio, como fallos que requieren intervención inmediata.
3. **Aprobación:** La propuesta de cambio se somete a aprobación. En esta fase se verifica que cumpla con los requisitos y estándares definidos, garantizando su alineación con los objetivos del servicio.
4. **Planificación:** Según su clasificación, se desarrolla un plan para la implementación del cambio, estableciendo actividades, cronograma y asignación de recursos.
5. **Implantación:** Se ejecuta el cambio, coordinando y supervisando todas las actividades necesarias para asegurar su correcta implementación y minimizando cualquier interrupción en los servicios.

Este proceso garantiza que cada cambio se maneje de forma estructurada y controlada, minimizando riesgos.

## 4\. PETICIONES DE CAMBIO

Las peticiones de cambio suelen originarse tanto de clientes y usuarios, quienes pueden plantear nuevas necesidades, como del equipo de desarrollo, ya sea debido a dificultades técnicas imprevistas, resolución de conflictos, o no conformidades con los requisitos actuales.

Cuando se presente una petición de cambio en los requisitos (PCR), esta deberá ser debidamente registrada para que el Director de proyecto o el Patrocinador pueda evaluar su aceptación o rechazo. Esta decisión se tomará tras el análisis exhaustivo del impacto del cambio en el proyecto definido en las fases de gestión del cambio, considerando aspectos como alcance, costo y cronograma.

La plantilla para los cambios en los requisitos es la siguiente

| <_id_>-999 | <_nombre descriptivo_> |
| --- | --- |
| Fecha | <_fecha de la petición del cambio_> |
| Autores | - <_persona que formaliza la petición_> <br> - … |
| Descripción | El cambio solicitado consiste en: <_descripción del cambio_>. |
| Elementos afectados | Los elementos directamente afectados por el cambio son: <br> - <_elemento afectado_> <br> - … |
| Justificación | El cambio solicitado se considera necesario por: <br> <_descripción de la justificación_> |
| Consecuencias del rechazo | En caso de rechazar el cambio, las posibles consecuencias son: <br> - <_consecuencia del rechazo_> <br> - … |
| [Comentarios] | <_comentarios adicionales sobre la petición de cambio_> |
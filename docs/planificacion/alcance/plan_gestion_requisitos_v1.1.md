---
title: "Plan de Gestión de los requisitos"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "13/10/2024"  # modificar
subject: "PGPI"
author: [Antonio Macías Ferrera, Rafael Pulido Cifuentes]
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

# PLAN DE GESTIÓN DE REQUISITOS

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces
- **CÓDIGO DEL PROYECTO:** 2.15
- **FECHA DE CREACIÓN:** 13/10/2024
- **VERSIÓN DEL DOCUMENTO:** 1.1

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO**

|Fecha	|Realizada por	|Breve descripción de los cambios |
| ----- | ------------- | ----------------- |
|02/10/2024	| Antonio Macías Ferrera, Rafael Pulido Cifuentes |	Elaboración de la primera versión del documento |

\newpage


# RECOPILACIÓN DE REQUISITOS

La obtención de los requisitos **se llevará a cabo principalmente a través de reuniones** con el cliente (Product Owner). Los primeros requisitos serán definidos a partir de los objetivos de alto nivel presentados en el acta de constitución y acordados con el cliente durante la primera reunión. A partir de estos, se detallarán los requisitos adicionales, siempre respetando las limitaciones técnicas de la tecnología seleccionada para el proyecto y sin salirse del alcance del proyecto.

<br>

Es importante destacar que **cualquier requisito que se salga del alcance inicialmente definido en el acta de constitución será excluido del proyecto**. Los requisitos podrán sufrir pequeñas variaciones tras la entrega de los prototipos, siempre que no impliquen la adición de nuevas funcionalidades. En caso de que se sugieran nuevos requisitos o cambios significativos, estos deberán ser validados por ambas partes y requerirán una revisión del presupuesto antes de ser incorporados al proyecto. Esta medida garantiza que cualquier modificación se gestione de manera controlada, evitando desviaciones inesperadas en el alcance y la planificación del proyecto.

<br>

# ANÁLISIS DE REQUISITOS

El análisis de los requisitos se realizará mediante un enfoque sistemático que incluye varias etapas clave. En primer lugar, se procederá a **clasificar los requisitos según su naturaleza**. A continuación, **se priorizarán estos requisitos de acuerdo con** su criticidad, utilizando **el método *MoSCoW***. Una vez priorizados, se evaluarán conforme a las métricas establecidas para garantizar su validez y pertinencia, asegurando que cumplen con las expectativas y necesidades de los *stakeholders*. Finalmente, todos los **requisitos serán documentados** de manera clara y precisa en el documento de requisitos, el cual servirá como referencia a lo largo del ciclo de vida del proyecto. Para asegurar la correcta trazabilidad de cada requisito, se implementará una **matriz de trazabilidad** que será de utilidad el seguimiento de la evolución de los requisitos desde su concepción hasta su implementación. Esta matriz permitirá identificar relaciones entre requisitos y objetivos facilitando el posible cambio o adición de nuevos requisitos.

<br>

Para analizar el cambio en un requisito previamente definido, igualmente se seguirá un proceso con varios pasos. Primero, se identifica el cambio a través de una **solicitud** detallada que especifique el nuevo requisito o la modificación y su justificación. Luego, se realiza un **análisis de trazabilidad** para identificar todas las áreas del proyecto afectadas, incluyendo módulos de software, casos de uso y documentación relevante. A continuación, se evalúa cómo el cambio impactará el **alcance**, considerando si requiere nuevas funcionalidades o ajustes en los recursos. Se analiza también el impacto en el **cronograma**, estimando el tiempo adicional necesario y utilizando herramientas de gestión de proyectos para recalcular las fechas de entrega. El impacto en el **presupuesto** se evalúa para asegurar que el cambio es económicamente viable, tomando en cuenta posibles costos ocultos.

<br>

La **calidad** del producto se revisa para garantizar que el cambio no afecte los estándares establecidos, y se realiza un análisis de **riesgos** para identificar nuevos riesgos potenciales. Con toda la información recopilada, se presenta el análisis para la **toma de decisiones** sobre la aprobación o rechazo del cambio. Finalmente, si el cambio se aprueba, se actualizan todos los documentos relevantes para mantener la consistencia del proyecto.

<br>

# CLASIFICACIÓN DE REQUISITOS

## **1. Requisitos del proyecto**
Los requisitos del proyecto son las condiciones o capacidades necesarias para cumplir los objetivos del proyecto en términos de tiempos, costos y recursos. Se enfocan en la planificación y gestión del proyecto, estableciendo restricciones y expectativas para garantizar su éxito.

## **2. Requisitos del producto**
Los requisitos del producto describen las características y funcionalidades que el sistema o software debe tener. Los dividiremos en dos categorías principales: funcionales y no funcionales.

### **2.1. Funcionales**
Son las capacidades específicas que el sistema debe proporcionar para cumplir con las expectativas del usuario. Estos describen técnicamente qué debe hacer el sistema a un más bajo nivel.
- **Requisitos de información**: especifican cómo el sistema debe gestionar, almacenar, y procesar la información (entrada, salida, y almacenamiento).
- **Requisitos de reglas de negocio:** definen las políticas, condiciones o reglas de negocio que el sistema debe seguir para funcionar correctamente.
- **Requisitos de conducta:** establecen el comportamiento que el sistema debe exhibir en ciertas situaciones o eventos, como reacciones a errores o acciones del usuario.

### **2.2. No funcionales**
Estos requisitos se enfocan en cómo el sistema debe funciona en diversos aspectos como la calidad, rendimiento, restricciones técnicas, etc.
- **Requisitos de fiabilidad**: Definen el nivel de confiabilidad que debe tener el sistema, especificando su capacidad para operar sin fallos durante un tiempo determinado.
- **Requisitos de usabilidad**: Se refieren a la facilidad de uso y la experiencia del usuario al interactuar con el sistema, evaluando aspectos como la interfaz y la accesibilidad.
- **Requisitos de mantenibilidad**: Especifican cuán fácil es actualizar, corregir errores y mantener el sistema a lo largo del tiempo.
- **Requisitos de eficiencia**: Involucran el uso de recursos del sistema, como el rendimiento en términos de tiempo de respuesta o el uso eficiente de espacio y memoria.
- **Requisitos de portabilidad**: Indican la capacidad del sistema para operar en diferentes entornos o plataformas sin requerir cambios significativos.
- **Requisitos de seguridad**: Establecen las medidas que se deben tomar para proteger el sistema y los datos del usuario contra accesos no autorizados, amenazas y ataques.

## **3. Requisitos de la organización**
Son aquellos que definen las normas y condiciones que la organización debe cumplir para la entrega y operación del sistema.

### **3.1. Requisitos de entrega**
Establecen los hitos importantes a lo largo de la ejecución del proyecto, los plazos de entrega y las condiciones en las que el sistema debe ser entregado al cliente.

### **3.2. Requisitos de uso de estándares**
Definen las normativas y estándares de calidad, seguridad o tecnología que el producto debe cumplir.

### **3.3. Requisitos de uso de tecnología**
Especifican las tecnologías que se deben emplear en el desarrollo y operación del sistema, tales como lenguajes de programación, plataformas o herramientas.

## **4. Requisitos de factores ambientales externos**
Estos requisitos son influenciados por factores externos a la organización, como la legislación o los acuerdos de privacidad.

### **4.1. Requisitos legislativos**
Son los requisitos que deben cumplir para asegurar que el sistema esté alineado con las leyes y regulaciones vigentes, como normativas gubernamentales, derechos de autor, o leyes laborales.

### **4.2. Requisitos de privacidad**
Establecen las pautas para garantizar la confidencialidad de los datos personales de los usuarios, asegurando su protección y evitando el mal uso de la información.

<br>

# DOCUMENTACIÓN DE REQUISITOS

La documentación de los requisitos el último paso que se realiza tras la validación de un nuevo requisito o el cambio de uno existente. Los documentos que se usarán en este proyecto para documentar los requisitos son el Documento de requisitos y las Matrices de trazabilidad.

<br>

- **Documento de requisitos:** Es el documento que recoge y describe de forma detallada todos los requisitos del proyecto. En el los requisitos quedan distinguidos en base a la clasificación de los mismos y cada uno de ellos recoge código, título, versión, autor(es), descripción, prioridad y urgencia. Adicionalmente podrá contener los campos comentarios y datos específicos si procediera. 
- **Matriz de trazabilidad:** Es la tabla que vincula cada requisito con el requisito de alto nivel del proyecto que le dio origen, realizar su seguimiento y control a lo largo de la ejecución del proyecto hasta el cierre.Se realizará una matriz para cada categoría de requisitos y otra para relacionar los requisitos que se correspondan con los objetivos del proyecto.

<br>

La documentación de los requisitos aporta una base sólida para la gestión del proyecto, ya que garantiza que todos los requisitos estén claramente definidos, priorizados y controlados. Con estos documentos se asegura la capacidad de adaptación e implementación conforme a lo planeado reduciendo la posibilidad de errores o malentendidos

<br>

# PRIORIZACIÓN DE REQUISITOS

A la hora de recoger los requisitos es fundamental la priorización de los mismos con el objetivo de establecer una jerarquía de importancia y urgencia clara, que resultará clave una vez que se lleve a cabo la implementación de cada uno de ellos. En este proyecto, los requisitos serán priorizados siguiendo el método *MoSCoW*, un método que se basa en la criticidad de los requisitos, es decir, la necesidad que tiene el proyecto de contar con unos u otros. De esta forma, el método *MoSCoW* establece 4 niveles de prioridad, siendo estos desde el mas crítico al menos crítico:

<br>

- **Must Have:** Es un requisito crítico para el éxito del proyecto.
- **Should Have**: Es un requisito importante pero no crítico para la entrega del proyecto.
- **Could Have:** Requisito deseable pero no necesario.
- **Won’t Have:** Requisito que se ha acordado que no es crítico ni necesario para el proyecto. Si fuese necesario por restricciones de tiempo o coste, estos requisitos podrían acabar en exclusiones del proyecto.

<br>

Por otro lado, a la hora de priorizar los requsitos dentro de estos 4 niveles, se establece el parámetro de la **urgencia**. Este indicador puede tomar valores del 1 al 3 indincando una mayor urgencia si toma un mayor valor. Con estos sistemas de priorización proporcionamos a los *stakeholders* una forma clara de visualizar requisitos que son o no críticos para el proyecto, y un lenguaje común para discutir las prioridades y expectativas del proyecto. Todo esto con el objetivo de simplificar el proceso de toma de decisiones con respecto a los requisitos. Al incluir la información esencial de cada requisito, se asegura que todos los involucrados comprendan claramente las necesidades y objetivos del proyecto.

<br>

# MÉTRICAS DE REQUISITOS

Las métricas de requisitos son medidas **cuantitativas** que permiten evaluar la calidad, consistencia y cumplimiento de los requisitos a lo largo del ciclo de vida del proyecto. A la hora de validar o analizar un requisito se hará uso de las siguientes métricas:

<br>

- **Tasa de cambios en los requisitos**: esto nos indica la frecuencia con la que los requisitos cambian durante el proyecto. Una alta tasa de cambios puede indicar problemas en la definición de requisitos o en la planificación inicial del proyecto.
- **Trazabilidad de requisitos**: el uso de la matriz de trazabilidad nos indica el grado en que los requisitos están relacionados con los objetivos del proyecto y los requisitos de más alto nivel acordados en el Acta de Constitución.
- **Satisfacción del cliente**: esta métrica se basa en la evaluación subjetiva por parte del cliente sobre cómo los requisitos han sido implementados y si cumplen sus expectativas. Esta es una métrica que será puesta en práctica durante la implementación del producto, en las reuniones periódicas que se podrán tener con el cliente. Esta métrica nos permitirá, además de corregir el producto en desarrollo, corregir posibles requisitos relacionados que todavía no han sido implementados y así disminuir el coste de futuras correcciones. 

<br>

# VALIDACIÓN DE REQUISITOS

La validación de requisitos es un proceso de asegurar que los requisitos del proyecto y del producto se alineen con las necesidades y expectativas del cliente. Consideramos que el uso estas técnicas de validación de requisitos son importantes para asegurar que el sistema final cumple con las expectativas del cliente y es eficiente en su desarrollo.

<br>

- El primer factor determinante a la hora de validar un requisito es su **trazabilidad**. Todos los requisitos del proyecto deben estar relacionados con al menos un requisito de alto nivel o un objetivo de proyecto de los acordados en el Acta de Constitución. 
- Las **revisiones a pares** serán otra forma de validación en la que el autor de unos requisitos revisará los requisitos elaborados por otro autor, y viceversa. Esta técnica permite identificar problemas en una etapa temprana y asegura que los requisitos sean de alta calidad antes de que el desarrollo avance.
- En última instancia, las **revisiones con el cliente** servirán como métrica de validación de requisitos, pudiendo corregir los requisitos ya implementados y revisados por el cliente, así como otros requisitos aún no implementados que compartan relación con los anteriores.

<br>

# TRAZABILIDAD DE REQUISITOS

La trazabilidad consideramos que es la métrica de validación de requisitos más importante ya que nos permite evaluar a simple vista la relación de cada requisito con un objetivo del proyecto o del producto. En concreto, se realizarán dos tipos de matrices de trazabilidad:
- Una matriz por cada grupo de requisitos de producto que relacione cada requisito con uno de los requisitos de alto nivel definidos en el Acta de Constitución.
- Otro grupo que relacione cada requisito ambiental, de proyecto u organizacional con un objetivo de proyecto. 

<br>

# INFORME DE REQUISITOS

La creación y actualización de los informes de requisitos se llevará a cabo de forma continua y sistemática. El objetivo principal es asegurar que todas las partes interesadas estén plenamente informadas sobre el progreso y cumplimiento de los requisitos establecidos. Además, se detallará el estado actual de cada requisito, lo que permitirá a los interesados tener una visión clara y precisa del desarrollo del proyecto. Esta práctica garantiza una comunicación efectiva y transparente, facilitando la toma de decisiones informadas y la identificación temprana de posibles problemas o desviaciones en el cumplimiento de los requisitos. 

<br>

# GESTIÓN DE LA CONFIGURACIÓN

Como parte de la gestión de los requisitos, se establecen los procedimientos y mecanismos necesarios para garantizar el control de versiones y la integridad de todos los productos de trabajo, tales como software, aplicaciones, planes, documentación, procedimientos internos y estándares. A lo largo del ciclo de desarrollo, se llevan a cabo actividades de gestión de la configuración, relacionadas tanto con solicitudes de cambio en los requisitos como con cambios internos. Estas actividades incluyen:

<br>

- **Registro de la Solicitud de Cambio**: Se formaliza la solicitud de un cambio mediante un formulario de petición de cambio.
- **Evaluación de la Solicitud de Cambio**: El equipo de desarrollo analiza el impacto de la solicitud, considerando aspectos como la afectación a los entregables, el esfuerzo necesario y las posibles repercusiones en los plazos del proyecto.
- **Decisión sobre Aceptación/Rechazo**: Basado en el análisis de impacto, se decide si el cambio será aceptado rechazado. Si se acepta, se determinará en qué iteración se implementará.
- **Implementación del Cambio**: El cambio se lleva a cabo de acuerdo con las actividades previamente planificadas.
- **Control de Cambios y Versiones**: Durante la implementación, se aplicará un control riguroso de versiones y de cambios sobre los elementos de configuración establecidos, cubriendo al menos todos los entregables del proyecto.

<br>

Este proceso asegura que los cambios sean gestionados de manera controlada y que el proyecto mantenga su integridad y coherencia a lo largo del tiempo.

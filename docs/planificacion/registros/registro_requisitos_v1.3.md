---
title: "Registro de requisitos"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "14/10/2024"  # modificar
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
\definecolor{orange1}{HTML}{EDBB99}
\definecolor{yellow1}{HTML}{F1C40F}
\definecolor{green1}{HTML}{52BE80}
\definecolor{purple1}{HTML}{9B59B6}

\definecolor{red1}{HTML}{EA2223}


# REGISTRO DE REQUISITOS

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces
- **CÓDIGO DEL PROYECTO:** 2.15
- **FECHA DE CREACIÓN:** 13/10/2024
- **VERSIÓN DEL DOCUMENTO:** 1.2

<br>

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO**

|Fecha	|Realizada por	|Breve descripción de los cambios |
| ----- | ------------- | ----------------- |
|02/10/2024	| Antonio Macías Ferrera |	Elaboración de la primera versión del documento |
|14/10/2024	| Antonio Macías Ferrera |	Correcciones de formato para la exportación a markdown |

\newpage



# **1. Requisitos del proyecto**

Los "requisitos del proyecto" son especificaciones detalladas que definen las funcionalidades, características y condiciones que debe cumplir un proyecto para ser considerado exitoso.

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PRQ-001} & \textbf{Entrega del proyecto} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & El proyecto debe cumplir con los términos de referencia del contrato suscrito entre las partes, y debe finalizar antes de su fecha límite el 06/12/2024. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PRQ-002} & \textbf{Accesibilidad del sistema} \\
\hline
\textbf{Versión} & 1.1 \\
\hline
\textbf{Autores} & Ramón Gavira Sánchez \\
\hline
\textbf{Descripción} & El sistema final debe tener un diseño apropiado y fácil de usar acorde a la edad de los ciudadanos de Villanueva de las Cruces y cumplir con el nivel AA de accesibilidad según el estándar WCAG 2.1 \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PRQ-003} & \textbf{Inicio de sesión} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Los ciudadanos usuarios del sistema deben acceder de forma fácil, sin necesidad de correos electrónicos u otros mecanismos más sofisticados \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PRQ-004} & \textbf{Información proporcionada}  \\ 
\hline
\textbf{Versión}   & 1.0 \\                    
\hline
\textbf{Autores}   & Rafael Pulido Cifuentes \\   
\hline
\textbf{Descripción} & El sistema debe proporcionar información actualizada acerca de los horarios y disponibilidad de los espacios de uso común \\ 
\hline
\textbf{Prioridad} & \textbf{Must} \\  
\hline                     
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{blue1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{blue1!50}
\textbf{PRQ-005} & \textbf{Entrega del proyecto}  \\ 
\hline
\textbf{Versión}   & 1.0 \\               
\hline
\textbf{Autores}   & Rafael Pulido Cifuentes \\  
\hline
\textbf{Descripción} & El sistema debe permitir a los usuarios tanto reservar los espacios de uso común como cancelar estas reservas. \\
\hline
\textbf{Prioridad} & \textbf{Must}   \\  
\hline        
\end{tabular}
\end{table}

\newpage

...

\newpage


# **2. Requisitos del producto**

Los "requisitos del producto" son un conjunto de especificaciones que describen las características, funciones y condiciones que un producto debe cumplir para satisfacer las necesidades y expectativas de los usuarios finales y otros interesados. Estos requisitos abarcan tanto aspectos funcionales, que indican qué debe hacer el producto, como no funcionales, que definen cómo debe comportarse en términos de rendimiento, seguridad, usabilidad y compatibilidad.

## **2.1 Requisitos funcionales del sistema**

### **2.1.1 Requisitos de información del sistema**

<br>

\begin{table}[!ht]
\centering
\rowcolors{1}{yellow1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{yellow1!50}
\textbf{IRQ-001} & \textbf{Información sobre los usuarios y clientes} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema debe almacenar la información correspondiente a los usuarios. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Datos específicos} & - Nombre \newline - Apellidos \newline - Teléfono (opcional) \newline - DNI \newline - Dirección postal \\
\hline
\textbf{Urgencia} & 1 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{yellow1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{yellow1!50}
\textbf{IRQ-002} & \textbf{Información sobre espacios públicos} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema debe almacenar la información de cada uno de los espacios públicos ofertados por el ayuntamiento de la localidad. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Datos específicos} & - Nombre \newline - Horario \newline - Descripción \newline - Fotos \newline - Teléfono de atención (opcional) \newline - Estado [RESERVADO, LIBRE, NO DISPONIBLE] \\
\hline
\textbf{Urgencia} & 1 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{yellow1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{yellow1!50}
\textbf{IRQ-003} & \textbf{Información sobre ayuntamiento} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema debe almacenar la información acerca del ayuntamiento de la localidad. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Datos específicos} & - Localidad \newline - Escudo de la localidad o del ayuntamiento \newline - Información de interés \newline - Teléfono de atención \newline - Correo electrónico de asistencia \newline - Foto de portada \\
\hline
\textbf{Urgencia} & 1 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{yellow1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{yellow1!50}
\textbf{IRQ-004} & \textbf{Información sobre las reservas} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema debe almacenar las reservas asociadas a cada espacio público. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Datos específicos} & - Fecha de realización \newline - Franja horaria seleccionada \newline - Estado [REALIZADA, CANCELADA, EN CURSO, FINALIZADA] \\
\hline
\textbf{Urgencia} & 1 \\
\hline
\end{tabular}
\end{table}

\FloatBarrier

\newpage


### **2.1.2 Requisitos de reglas de negocio del sistema**


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{CRQ-001} & \textbf{Creación de un espacio público} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Solo un administrador del ayuntamiento de la localidad podrá añadir nuevos espacios públicos. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 2 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{CRQ-002} & \textbf{Modificación de un espacio público} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Solo un administrador del ayuntamiento de la localidad podrá modificar los datos de un espacio público existente. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 2 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{CRQ-003} & \textbf{Eliminación de un espacio público} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Solo un administrador del ayuntamiento de la localidad podrá eliminar un espacio público existente. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 2 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{CRQ-004} & \textbf{Acceso a la aplicación} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Un usuario de la aplicación solo podrá acceder a ella si está censado en el ayuntamiento de la localidad. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 1 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{CRQ-005} & \textbf{Modificación de un usuario} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Un usuario no podrá modificar sus datos, ya que la información de los usuarios que se registren es proporcionada por el ayuntamiento de la localidad. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 2 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{CRQ-006} & \textbf{Visualización de espacios públicos} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Solo los usuarios censados en la localidad tendrán acceso a consultar los espacios públicos de esta. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 2 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{CRQ-007} & \textbf{Realización de una reserva} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Solo los usuarios censados en la localidad podrán reservar espacios públicos de esta. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 2 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{CRQ-008} & \textbf{Disponibilidad de un espacio público} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Un usuario podrá realizar la reserva de un espacio público siempre y cuando el espacio esté marcado como LIBRE en la franja horaria seleccionada. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 2 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{CRQ-009} & \textbf{Modificación de una reserva} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Un usuario solo podrá modificar los datos de una reserva a su nombre, pudiendo cambiar la hora de la reserva, el espacio que solicita o bien cancelar la reserva. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 2 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{CRQ-010} & \textbf{Visualización de las reservas} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Un usuario solo podrá ver las reservas a su nombre, mientras que un administrador podrá visualizar todas las reservas de la localidad. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 2 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{CRQ-011} & \textbf{Eliminación de los datos} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Un usuario podrá solicitar la eliminación del registro de todas sus reservas realizadas. \\
\hline
\textbf{Prioridad} & \textbf{Should} \\
\hline
\textbf{Urgencia} & 2 \\
\hline
\textbf{Comentario} & Otros datos como el DNI no se eliminarán, ya que realmente pertenecen al ayuntamiento. \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{CRQ-012} & \textbf{Indisponibilidad de un espacio público} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Si un administrador tiene que reservar un espacio por un evento extraordinario y esto afecta a una reserva ya realizada en este u otros espacios públicos, la reserva deberá ser cancelada. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 3 \\
\hline
\textbf{Comentario} & El usuario deberá ser notificado vía SMS y/o con una alerta en la aplicación. \\
\hline
\end{tabular}
\end{table}

\FloatBarrier

\newpage


### **2.1.3 Requisitos de conducta del sistema**

\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{COR-001} & \textbf{Disponibilidad de los espacios públicos} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Si un espacio público es marcado como INDISPONIBLE por algún evento extraordinario, deberá mostrar una alerta informativa al consultar el espacio dentro de la aplicación. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 3 \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{green1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{green1!50}
\textbf{COR-002} & \textbf{Aceptación del reglamento de protección de datos} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & Se deberá pedir el consentimiento del usuario para el tratamiento de sus datos la primera vez que inicie sesión en la aplicación. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\textbf{Urgencia} & 3 \\
\hline
\end{tabular}
\end{table}


\newpage



## **2.2 Requisitos no funcionales del sistema**


### **2.2.1 Requisitos de fiabilidad del sistema**

\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{NFR-001} & \textbf{Adaptabilidad de la página web} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & La disponibilidad de los espacios debe reflejarse en tiempo real y evitar conflictos de reservas duplicadas o inconsistencias entre usuarios y administradores. \\
\hline
\textbf{Prioridad} & \textbf{Should} \\
\hline
\end{tabular}
\end{table}

<br>

### **2.2.2 Requisitos de usabilidad del sistema**

\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{NFR-002} & \textbf{Adaptabilidad de la página web} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema deberá adaptarse al tipo de dispositivo desde el que se acceda, es decir, que tenga un diseño responsive. \\
\hline
\textbf{Prioridad} & \textbf{Should} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{NFR-003} & \textbf{Inicio de sesión accesible} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El usuario deberá poder acceder a la aplicación de forma fácil, simplemente ingresando su DNI y fecha de nacimiento para poder ser identificado por el censo del ayuntamiento. Los datos serán comprobados en una base de datos proporcionada por el ayuntamiento. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{NFR-004} & \textbf{Interfaz accesible} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema deberá contener una interfaz simple e intuitiva, preparada para ser accesible para personas mayores. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}



\newpage


### **2.2.3 Requisitos de mantenibilidad del sistema**

Aunque no nos comprometemos a realizar un despliegue y mantenimiento de la aplicación funcional, nos comprometemos con los siguientes requisitos de mantenibilidad acorde con su prioridad:

\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{NFR-005} & \textbf{Mantenibilidad del código} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El código fuente del sistema deberá seguir los ‘coding standards’ adecuados al lenguaje de programación, así como estar debidamente organizado y comentado. \\
\hline
\textbf{Prioridad} & \textbf{Could} \\
\hline
\end{tabular}
\end{table}


### **2.2.4 Requisitos de eficiencia del sistema**


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{NFR-006} & \textbf{Disponibilidad del sistema} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & La disponibilidad del sistema debe ser del 99\%, asegurando acceso constante a la BD. \\
\hline
\textbf{Prioridad} & \textbf{Could} \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{NFR-007} & \textbf{Tiempo de carga de las distintas vistas} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema debe cargar en un tiempo no superior a 1 seg, trayendo únicamente los datos necesarios en cada vista. \\
\hline
\textbf{Prioridad} & \textbf{Could} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{NFR-008} & \textbf{Tiempo de carga inicial de la web} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema debe cargar en un tiempo no superior a 5 segundos. \\
\hline
\textbf{Prioridad} & \textbf{Could} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{NFR-009} & \textbf{Limitar las solicitudes} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema deberá limitar las solicitudes por minuto, por ejemplo, a 100, para no sufrir un colapso de esta. \\
\hline
\textbf{Prioridad} & \textbf{Could} \\
\hline
\end{tabular}
\end{table}


### **2.2.5 Requisitos de portabilidad del sistema**

\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{NFR-010} & \textbf{Varios navegadores} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema deberá estar disponible en distintos navegadores, ya pueden ser Chrome, Firefox, etc. \\
\hline
\textbf{Prioridad} & \textbf{Should} \\
\hline
\end{tabular}
\end{table}


\newpage


### **2.2.6 Requisitos de seguridad del sistema**

\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{NFR-011} & \textbf{Funcionalidades de las cuentas} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema debe asegurar que cada rol disponible en la web pueda cumplir únicamente sus funciones designadas, sin acceso a las funciones de otros roles. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{orange1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{orange1!50}
\textbf{NFR-012} & \textbf{Base de datos a prueba de ataques} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema debe estar protegido contra varios tipos de ataques a la base de datos, ya que contendrá información importante, incluyendo datos confidenciales. \\
\hline
\textbf{Prioridad} & \textbf{Should} \\
\hline
\end{tabular}
\end{table}

\newpage

# 3. **Requisitos de la organización**
## **3.1. Requisitos de entrega** 


\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{DRQ-001} & \textbf{Formato de entrega del software} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Todo el software desarrollado que se entregue al cliente debe ser entregado en formato comprimido (.zip, .7zip…) \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{DRQ-002} & \textbf{Plazos de entrega} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Todos los productos (documentos, software, actas…) deben ser entregados dentro del plazo acordado con el cliente \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{DRQ-003} & \textbf{Validación de los entregables} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Todos los productos entregados deben haber sido previamente validados de acuerdo con las métricas establecidas \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{DRQ-004} & \textbf{Calidad de los entregables} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Todos los productos entregados deben cumplir los niveles de calidad establecidos. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}


\newpage


## **3.2. Requisitos de uso de estándares**


\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{USR-001} & \textbf{Estándar de seguridad} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Los datos almacenados y transmitidos por la aplicación deben cumplir con los estándares de seguridad especificados en el Reglamento General de Protección de Datos (GDPR) para asegurar la protección de la información sensible. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{USR-002} & \textbf{Estándar de mejora continua} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & El sistema de actividades de mejora continua debe seguir la estructura del Ciclo de Deming, con intención de mejorar los procesos y actividades que se repiten múltiples veces en el cronograma. \\
\hline
\textbf{Prioridad} & \textbf{Should} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{USR-003} & \textbf{Estándar gestión de proyecto} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & A nivel global, todos los procesos del proyecto actual deben seguir el estándar proporcionado por PMBOK. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{USR-004} & \textbf{Estándar de versionado} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Todos los productos software que sean etiquetados con una versión deben seguir el estándar de versionado semántico. \\
\hline
\textbf{Prioridad} & \textbf{Should} \\
\hline
\end{tabular}
\end{table}


\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{USR-005} & \textbf{Estándar de programación} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Los productos software deben ser desarrollados siguiendo las prácticas de *Pair Programming*. \\
\hline
\textbf{Prioridad} & \textbf{Could} \\
\hline
\end{tabular}
\end{table}


\newpage


## **3.3.  Requisitos de uso de tecnología**##


\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{UTR-001} & \textbf{Lenguaje de desarrollo BackEnd} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Todo el desarrollo BackEnd del proyecto debe realizarse en lenguaje Python. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{UTR-002} & \textbf{Lenguaje de desarrollo FrontEnd} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & El desarrollo FrontEnd del proyecto debe realizarse con JavaScript, HTML y CSS. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}

\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{UTR-003} & \textbf{Framework de desarrollo} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & El desarrollo del proyecto debe realizarse utilizando el Framework Django. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{UTR-004} & \textbf{Herramienta de gestión} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & El proyecto debe ser gestionado (cronogramas, recursos, tareas…) utilizando la herramienta MSProject. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{UTR-005} & \textbf{Repositorio del proyecto} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Todos los productos software deben ser almacenados en el repositorio del proyecto (pueblista-pgpi). \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{UTR-006} & \textbf{Seguimiento del rendimiento} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Para el seguimiento del rendimiento del equipo de desarrollo durante el proyecto se debe hacer uso de la herramienta ZenHub. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{red1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{red1!50}
\textbf{UTR-007} & \textbf{Computación de horas} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Para la computación de las horas empleadas durante el proyecto, cada miembro del equipo deberá usar la herramienta Clockify. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}

\newpage

...

\newpage


# **4. Requisitos de factores ambientales externos** 
## **4.1. Requisitos legislativos**

\begin{table}[!ht]
\centering
\rowcolors{1}{purple1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{purple1!50}
\textbf{AFR-001} & \textbf{Ley Orgánica de Protección de Datos Personales y garantía de los derechos digitales} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Antonio Macías Ferrera \\
\hline
\textbf{Descripción} & El sistema deberá cumplir la Ley Orgánica de Protección de Datos Personales y garantía de los derechos digitales, ya que registrará bastantes datos personales. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}





## **4.2. Requisitos de privacidad**


\begin{table}[!ht]
\centering
\rowcolors{1}{purple1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{purple1!50}
\textbf{PRR-001} & \textbf{Acceso y control de datos} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & El sistema debe permitir a los usuarios acceder a sus datos y solicitar su eliminación. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{purple1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{purple1!50}
\textbf{PRR-002} & \textbf{Uso de los datos} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Los datos recopilados solo se utilizarán como método de identificación del usuario como persona censada y no se compartirán con terceros sin el consentimiento del usuario. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{purple1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{purple1!50}
\textbf{PRR-003} & \textbf{Almacenamiento y seguridad de datos} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & Los datos personales deben ser almacenados en servidores seguros y se aplicarán controles de acceso para garantizar su seguridad. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}



\begin{table}[!ht]
\centering
\rowcolors{1}{purple1!25}{white}
\begin{tabular}{|p{4cm}|p{10cm}|}
\hline
\rowcolor{purple1!50}
\textbf{PRR-004} & \textbf{Notificación de violaciones de datos} \\
\hline
\textbf{Versión} & 1.0 \\
\hline
\textbf{Autores} & Rafael Pulido Cifuentes \\
\hline
\textbf{Descripción} & En caso de violación de datos, se debe notificar a los usuarios dentro de las 72 horas posteriores a la detección de la brecha. \\
\hline
\textbf{Prioridad} & \textbf{Must} \\
\hline
\end{tabular}
\end{table}



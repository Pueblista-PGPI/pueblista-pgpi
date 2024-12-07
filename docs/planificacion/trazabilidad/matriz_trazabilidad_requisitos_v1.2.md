---
title: "Matriz de trazabilidad de requisitos"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "13/10/2024"  # modificar
subject: "PGPI"
author: [Daniel Fernández Caballero, Ramón Gavira Sánchez, José Miguel Iborra Conejo, Antonio Macías Ferrera, Rafael Pulido Cifuentes]
lang: "es"
toc: true
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
    - \usepackage{graphicx}
    - \usepackage{changepage}
---

\definecolor{blue1}{HTML}{5DADE2}



**MATRIZ DE TRAZABILIDAD DE REQUISITO**

- **NOMBRE DEL PROYECTO:** Pueblista: Diseño, desarrollo e implantación de una aplicación web para la reserva de espacios públicos en pequeños municipios andaluces
- **CÓDIGO DEL PROYECTO:** 2.15
- **FECHA DE CREACIÓN:** 13/10/2024
- **VERSIÓN DEL DOCUMENTO:** 1.2

**HISTÓRICO DE MODIFICACIONES DEL DOCUMENTO**

|Fecha	|Realizada por	|Breve descripción de los cambios |
| ----- | ------------- | ----------------- |
|02/10/2024	| Antonio Macías Ferrera |	Elaboración de la primera versión de la matriz de trazabilidad. |
|30/11/2024	| Antonio Macías Ferrera |	Corrección y mejora de formato de las tablas. |

\newpage

# 1. REQUISITOS A NIVEL DE PROYECTO

Para realizar la matriz de trazabilidad respecto a los requisitos de proyecto, organización y factores ambientales, recordamos que los objetivos del proyecto a cumplir eran los siguientes:

**OBJ – 001**: El proyecto debe cumplir con los términos de referencia del contrato que se firme con el cliente y debe finalizar antes de la fecha límite del 06/12/2024.

**OBJ – 002**: Involucrar al cliente en las actividades relevantes del proyecto, para garantizar el éxito de este, obtener un alto grado de satisfacción y confianza de cara a futuros proyectos.

**OBJ – 003**: Aumentar la satisfacción de los habitantes del pueblo y el uso de estos espacios públicos.

**OBJ – 004**: Mejorar la eficiencia del pueblo en la gestión de reservas de espacios públicos, reduciendo el tiempo y los recursos necesarios en comparación con el método tradicional de reservas.

**OBJ – 005**: Aumentar la adopción de tecnologías digitales en el municipio.


<br>

\begin{longtable}{|>{\raggedright\arraybackslash}p{2cm}|p{2cm}|p{2cm}|p{2cm}|p{2cm}|p{2cm}|}
\hline
\rowcolor{blue1!50}
\textbf{Requisito} & \textbf{OBJ-001} & \textbf{OBJ-002} & \textbf{OBJ-003} & \textbf{OBJ-004} & \textbf{OBJ-005} \\
\hline
\endfirsthead

\hline
\rowcolor{blue1!50}
\textbf{Requisito} & \textbf{OBJ-001} & \textbf{OBJ-002} & \textbf{OBJ-003} & \textbf{OBJ-004} & \textbf{OBJ-005} \\
\hline
\endhead

\hline
\endfoot

\hline
\endlastfoot

\textbf{PRQ-001} & X & & & & \\
\hline
\textbf{PRQ-002} & & & & & X \\
\hline
\textbf{PRQ-003} & & & & & X \\
\hline
\textbf{PRQ-004} & & & & X & \\
\hline
\textbf{PRQ-005} & & & X & & \\
\hline
\textbf{DRQ-001} & X & & & & \\
\hline
\textbf{DRQ-002} & X & & & & \\
\hline
\textbf{DRQ-003} & & X & & & \\
\hline
\textbf{DRQ-004} & & X & & & \\
\hline
\textbf{USR-001} & & X & & & \\
\hline
\textbf{USR-002} & & X & & & \\
\hline
\textbf{USR-003} & & X & & & \\
\hline
\textbf{USR-004} & & X & & & \\
\hline
\textbf{USR-005} & & X & & & \\
\hline
\textbf{UTR-001} & & X & & & \\
\hline
\textbf{UTR-002} & & X & & & \\
\hline
\textbf{UTR-003} & & X & & & \\
\hline
\textbf{UTR-004} & & X & & & \\
\hline
\textbf{UTR-005} & & X & & & \\
\hline
\textbf{UTR-006} & & X & & & \\
\hline
\textbf{UTR-007} & & X & & & \\
\hline
\textbf{AFR-001} & X & & & & \\
\hline
\textbf{PRR-001} & X & & & & \\
\hline
\textbf{PRR-002} & X & & & & \\
\hline
\textbf{PRR-003} & X & & & & \\
\hline
\textbf{PRR-004} & X & & & & \\
\hline
\end{longtable}


\newpage


# 2. REQUISITOS A NIVEL DE PRODUCTO

Por otro lado, para realizar la matriz de trazabilidad de los requisitos del sistema, recordaremos los requisitos de alto nivel establecidos en el Acta de Constitución:

**RQM – 001**: El cliente quiere que la aplicación web tenga un diseño apropiado y fácil de usar acorde a la edad de los ciudadanos de Villanueva de las Cruces.

**RQM – 002**: El cliente quiere asegurarse de que los ciudadanos puedan consultar el horario y la disponibilidad de lugares de uso común del pueblo, procurando que sean siempre correctos.

**RQM – 003**: El cliente quiere que el horario y la disponibilidad de los espacios pueda ser actualizado y mantenido por los administradores del ayuntamiento.

**RQM – 004**: El cliente quiere que los ciudadanos puedan reservar los espacios de uso común del pueblo y cancelar las mismas.

**RQM – 005**: El cliente quiere que los ciudadanos puedan acceder a la aplicación de forma fácil, sin necesidad de correos electrónicos ni otros mecanismos más sofisticados.

**RQM – 006**: Cumplir con las normativas de protección de datos (como el RGPD), garantizando que la información de los usuarios esté segura y que se respete su privacidad.



## 2.1. REQUISITOS FUNCIONALES


\begin{longtable}{|>{\raggedright\arraybackslash}p{2cm}|p{2cm}|p{2cm}|p{2cm}|p{2cm}|p{2cm}|p{2cm}|}
\hline
\rowcolor{blue1!50}
\textbf{Requisito} & \textbf{RQM-001} & \textbf{RQM-002} & \textbf{RQM-003} & \textbf{RQM-004} & \textbf{RQM-005} & \textbf{RQM-006} \\
\hline
\endfirsthead

\hline
\rowcolor{blue1!50}
\textbf{Requisito} & \textbf{RQM-001} & \textbf{RQM-002} & \textbf{RQM-003} & \textbf{RQM-004} & \textbf{RQM-005} & \textbf{RQM-006} \\
\hline
\endhead

\hline
\endfoot

\hline
\endlastfoot

\textbf{IRQ-001} & X & & & & & \\
\hline
\textbf{IRQ-002} & & X & & & & \\
\hline
\textbf{IRQ-003} & & X & & & & \\
\hline
\textbf{IRQ-004} & & & & X & & \\
\hline
\textbf{CRQ-001} & & & X & & & \\
\hline
\textbf{CRQ-002} & & & X & & & \\
\hline
\textbf{CRQ-003} & & & X & & & \\
\hline
\textbf{CRQ-004} & & & & & X & \\
\hline
\textbf{CRQ-005} & & X & & & & \\
\hline
\textbf{CRQ-006} & & X & & & & \\
\hline
\textbf{CRQ-007} & & & & X & & \\
\hline
\textbf{CRQ-008} & & & & X & & \\
\hline
\textbf{CRQ-009} & & & & X & & \\
\hline
\textbf{CRQ-010} & & & & X & & \\
\hline
\textbf{CRQ-011} & & & & & & X \\
\hline
\textbf{CRQ-012} & & & X & & & \\
\hline
\textbf{COR-001} & & & X & & & \\
\hline
\textbf{COR-002} & & & & & & X \\
\hline
\end{longtable}


## 2.2. REQUISITOS NO FUNCIONALES


\begin{longtable}{|>{\raggedright\arraybackslash}p{2cm}|p{2cm}|p{2cm}|p{2cm}|p{2cm}|p{2cm}|p{2cm}|}
\hline
\rowcolor{blue1!50}
\textbf{Requisito} & \textbf{RQM-001} & \textbf{RQM-002} & \textbf{RQM-003} & \textbf{RQM-004} & \textbf{RQM-005} & \textbf{RQM-006} \\
\hline
\endfirsthead

\hline
\rowcolor{blue1!50}
\textbf{Requisito} & \textbf{RQM-001} & \textbf{RQM-002} & \textbf{RQM-003} & \textbf{RQM-004} & \textbf{RQM-005} & \textbf{RQM-006} \\
\hline
\endhead

\hline
\endfoot

\hline
\endlastfoot

\textbf{NFR-001} & & X & & & & \\
\hline
\textbf{NFR-002} & X & & & & & \\
\hline
\textbf{NFR-003} & & & & & X & \\
\hline
\textbf{NFR-004} & X & & & & & \\
\hline
\textbf{NFR-005} & & & X & & & \\
\hline
\textbf{NFR-006} & & X & X & & & \\
\hline
\textbf{NFR-007} & & X & X & & & \\
\hline
\textbf{NFR-008} & & X & X & & & \\
\hline
\textbf{NFR-009} & & X & X & & & \\
\hline
\textbf{NFR-010} & & & & & & X \\
\hline
\textbf{NFR-011} & & & & & & X \\
\hline
\textbf{NFR-012} & & & & & & X \\
\hline
\end{longtable}



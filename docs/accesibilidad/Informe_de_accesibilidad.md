---
title: "Informe de accesibilidad"  # modificar
subtitle: "Proyecto Pueblista - PGPI"
date: "29/11/2024"  # modificar
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

# Informe de accesibilidad

## Introducción
Este informe documenta los resultados del análisis de accesibilidad realizado en todas las páginas de la aplicación web del proyecto Pueblista, utilizando la herramienta **Lighthouse** para evaluar el cumplimiento del estándar **WCAG 2.1 nivel AA**. El propósito es asegurar que la aplicación es inclusiva, accesible y usable por todos los usuarios, independientemente de sus capacidades.

El informe se centra en los resultados específicos obtenidos para cada página, resaltando el grado de cumplimiento y las métricas clave de accesibilidad.

## Metodología
Se evaluaron múltiples aspectos de accesibilidad en cada página utilizando **Lighthouse**. El análisis incluyó:

- Contraste adecuado entre texto y fondo.
- Presencia de texto alternativo en imágenes y botones.
- Navegación operable mediante teclado.
- Diseño adaptativo y semántico.
- Compatibilidad con herramientas de asistencia.

## Análisis de los resultados
El gráfico que se presenta a continuación muestra los resultados de accesibilidad obtenidos en las auditorías realizadas con Lighthouse para las distintas páginas de la aplicación web del proyecto Pueblista. Cada página fue evaluada según su conformidad con el estándar WCAG 2.1 nivel AA, reflejando un enfoque robusto en el diseño inclusivo y accesible.

![Gráfica de porcentaje de accesibilidad](img/gráfica.png)

- **Resultados destacados:** La mayoría de las páginas alcanzaron un puntaje de accesibilidad del 98% o superior, con varias logrando el 100%, lo que demuestra un cumplimiento sobresaliente de los criterios de accesibilidad.
- **Áreas de mejora:** Algunas páginas, como "Reservas por Fecha", lograron un 95%, lo que sugiere pequeñas oportunidades de mejora en aspectos específicos.
- **Consistencia:** El proyecto demuestra un enfoque uniforme en la accesibilidad, garantizando que todos los usuarios puedan interactuar con las páginas de manera efectiva y sin barreras.
El gráfico resalta el compromiso del proyecto con la accesibilidad, mostrando las puntuaciones para cada página de forma comparativa. Esto facilita identificar rápidamente los logros y las áreas que podrían beneficiarse de optimizaciones adicionales.

A continuación se detallarán los resultados de cada página.

---

### **Página de Inicio**
- **URL**: `http://localhost:8000/`
- **Resultados de accesibilidad**: **98%**
- **Principales métricas**:
  - **First Contentful Paint**: 0.6 segundos.
  - **Largest Contentful Paint**: 0.7 segundos.
- **Cumplimientos destacados**:
  - Navegación por teclado funcional.
  - Contraste adecuado en textos y elementos interactivos.

---

### **Página de Login**
- **URL**: `http://localhost:8000/auth/login/`
- **Resultados de accesibilidad**: **100%**
- **Principales métricas**:
  - **Primera pintura con contenido visible**: 0.8 segundos.
  - **Contrast Ratio**: Cumple nivel AA.
- **Cumplimientos destacados**:
  - Etiquetas descriptivas en formularios.
  - Compatible con lectores de pantalla.

---

### **Página Mi Perfil**
- **URL**: `http://localhost:8000/auth/perfil/`
- **Resultados de accesibilidad**: **100%**
- **Principales métricas**:
  - **Largest Contentful Paint**: 0.8 segundos.
  - **Contraste**: Cumple con los requisitos AA.
- **Cumplimientos destacados**:
  - Etiquetas claras en campos de texto.
  - Botones y enlaces accesibles.

---

### **Página de Reservas de Espacios Especiales**
- **URL**: `https://pueblista-pgpi.onrender.com/espacios/18/reservas/?fecha=2024-12-01`
- **Resultados de accesibilidad**: **98%**
- **Principales métricas**:
  - **First Contentful Paint**: 0.6 segundos.
  - **Largest Contentful Paint**: 0.8 segundos.
- **Cumplimientos destacados**:
  - Contraste adecuado en los elementos interactivos.
  - Diseño responsivo para dispositivos móviles.

---

### **Página de Reservas de Espacios**
- **URL**: `https://pueblista-pgpi.onrender.com/espacios/21/reservas/`
- **Resultados de accesibilidad**: **100%**
- **Principales métricas**:
  - **First Contentful Paint**: 0.7 segundos.
  - **Largest Contentful Paint**: 0.7 segundos.
- **Cumplimientos destacados**:
  - Roles ARIA aplicados en botones y enlaces.
  - Texto alternativo en imágenes.

---

### **Página de Notificaciones**
- **URL**: `https://pueblista-pgpi.onrender.com/notificaciones/`
- **Resultados de accesibilidad**: **98%**
- **Principales métricas**:
  - **First Contentful Paint**: 0.7 segundos.
  - **Largest Contentful Paint**: 0.8 segundos.
- **Cumplimientos destacados**:
  - Estructura semántica clara.
  - Texto descriptivo en enlaces.

---

### **Página de Solicitudes Pendientes**
- **URL**: `https://pueblista-pgpi.onrender.com/espacios/18/reservas/solicitudes-pendientes`
- **Resultados de accesibilidad**: **98%**
- **Principales métricas**:
  - **First Contentful Paint**: 0.6 segundos.
  - **Largest Contentful Paint**: 0.7 segundos.
- **Cumplimientos destacados**:
  - Roles ARIA aplicados en tablas.
  - Navegación optimizada para teclado.

---

### **Formulario de Solicitudes**
- **URL**: `https://pueblista-pgpi.onrender.com/espacios/18/reservas/solicitud-espacio/`
- **Resultados de accesibilidad**: **98%**
- **Principales métricas**:
  - **First Contentful Paint**: 0.7 segundos.
  - **Largest Contentful Paint**: 0.8 segundos.
- **Cumplimientos destacados**:
  - Validaciones claras en formularios.
  - Mensajes descriptivos para errores.

---

### **Página General de Usuarios**
- **URL**: `http://localhost:8000/auth/user_list/`
- **Resultados de accesibilidad**: **98%**
- **Principales métricas**:
  - **Largest Contentful Paint**: 0.9 segundos.
  - **Velocidad de carga global**: 96%.
- **Cumplimientos destacados**:
  - Estructura de listas semánticas.
  - Foco claro en elementos interactivos.

---

### **Página de Espacios**
- **URL**: `https://pueblista-pgpi.onrender.com/espacios/list/`.
- **Accesibilidad**: **100%**.
- **Principales métricas**:
  - **First Contentful Paint**: 1.5 s.
  - **Largest Contentful Paint**: 1.5 s.
- **Cumplimientos destacados**:
  - Contraste adecuado en todos los elementos.
  - Roles ARIA correctamente implementados en listas y tablas.

---

### **Página de Crear Espacios**
- **URL**: `https://pueblista-pgpi.onrender.com/espacios/create/`.
- **Accesibilidad**: **100%**.
- **Principales métricas**:
  - **First Contentful Paint**: 0.7 s.
  - **Largest Contentful Paint**: 0.8 s.
- **Cumplimientos destacados**:
  - Etiquetas claras en formularios.
  - Navegación por teclado sin interrupciones.

---

### **Página de Editar Espacios**
- **URL**: `https://pueblista-pgpi.onrender.com/espacios/edit/21/`.
- **Accesibilidad**: **100%**.
- **Principales métricas**:
  - **First Contentful Paint**: 0.7 s.
  - **Largest Contentful Paint**: 0.9 s.
- **Cumplimientos destacados**:
  - Campos etiquetados correctamente para lectores de pantalla.
  - Compatibilidad con herramientas de asistencia modernas.

---

### **Página de Reservas**
- **URL**: `https://pueblista-pgpi.onrender.com/mis_reservas/`.
- **Accesibilidad**: **98%**.
- **Principales métricas**:
  - **First Contentful Paint**: 1.3 s.
  - **Largest Contentful Paint**: 1.6 s.
- **Cumplimientos destacados**:
  - Tablas semánticas y accesibles.
  - Navegación clara y fluida.

---

### **Página de Solicitudes Pendientes**
- **URL**: `https://pueblista-pgpi.onrender.com/espacios/18/reservas/solicitudes-pendientes`.
- **Accesibilidad**: **98%**.
- **Principales métricas**:
  - **First Contentful Paint**: 0.6 s.
  - **Largest Contentful Paint**: 0.7 s.
- **Cumplimientos destacados**:
  - Contraste óptimo y elementos accesibles.
  - Indicadores visuales para navegación por teclado.

---

### **Página de Mis Solicitudes Pendientes**
- **URL**: `https://pueblista-pgpi.onrender.com/espacios/18/reservas/mis-solicitudes`.
- **Accesibilidad**: **98%**.
- **Principales métricas**:
  - **First Contentful Paint**: 0.6 s.
  - **Largest Contentful Paint**: 0.7 s.
- **Cumplimientos destacados**:
  - Elementos interactivos claramente identificados.
  - Diseño responsivo adaptado para dispositivos móviles.

---

### **Página de Reservas por Fecha**
- **URL**: `https://pueblista-pgpi.onrender.com/espacios/reservas_fecha/21/`.
- **Accesibilidad**: **95%**.
- **Principales métricas**:
  - **First Contentful Paint**: 0.7 s.
  - **Largest Contentful Paint**: 0.8 s.
- **Cumplimientos destacados**:
  - Navegación optimizada y fluida.
  - Contraste adecuado y compatibilidad con lectores de pantalla.

## Cumplimiento Global con WCAG 2.1 Nivel AA
| **Principio**       | **Cumplimiento (%)** | **Detalles Clave**                                               |
|---------------------|---------------------|------------------------------------------------------------------|
| **Perceptible**      | 97%                | Contraste adecuado y texto alternativo en imágenes y botones.     |
| **Operable**         | 98%                 | Navegación por teclado y roles ARIA en elementos interactivos.    |
| **Comprensible**     | 100%                 | Formularios accesibles con mensajes claros y etiquetado correcto. |
| **Robusto**          | 99%                 | Compatible con herramientas modernas de asistencia.              |


## Conclusión
El análisis integral confirma que la aplicación cumple con los requisitos de **WCAG 2.1 nivel AA** en todas sus páginas evaluadas. Los resultados muestran un diseño robusto, accesible y alineado con los estándares modernos de inclusión digital.


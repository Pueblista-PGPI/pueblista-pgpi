<p align="center">
    <img src="pueblista/static/images/home/logo hd.png" align="center" width="30%">
</p>
<p align="center"><h1 align="center">PUEBLISTA</h1></p>
<p align="center">
    <em><code>Una aplicación web para reservar y gestionar espacios públicos de forma sencilla y eficiente.



</code></em>
</p>
<p align="center">
    <img src="https://img.shields.io/github/last-commit/Pueblista-PGPI/pueblista-pgpi?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/Pueblista-PGPI/pueblista-pgpi?style=default&color=0080ff" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/Pueblista-PGPI/pueblista-pgpi?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
    <!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Descripción general ](#descripcion-general)
- [ Características ](#caracteristicas)
- [ Estructura del proyecto ](#estructura-del-proyecto)
  - [ Índice del proyecto ](#indice-del-proyecto)
- [ Empezando ](#empezando)
  - [ Prerrequisitos ](#prerrequisitos)
  - [ Instalación ](#instalacion)
  - [ Uso ](#uso)
  - [ Pruebas ](#pruebas)
- [ Licencia ](#licencia)
- [ Autores ](#autores)

---

##  Descripción general

Pueblista es una aplicación web diseñada específicamente para facilitar la gestión y reserva de espacios públicos en Villanueva de las Cruces.
Gracias a esta herramienta, los habitantes empadronados en el municipio pueden consultar la disponibilidad de espacios, realizar reservas de forma autónoma y recibir confirmaciones automáticas.

La aplicación busca, por un lado, mejorar la organización y la accesibilidad a los espacios municipales para los habitantes del pueblo, y por otro lado, mejorar la eficiencia y agilizar la gestión de los recursos municipales, eliminando los métodos rudimentarios utilizados
anteriormente, como tablones físicos y reservas telefónicas.

**Este proyceto está desplegado de forma totalmete funcional el *Render*, y puedes acceder al él directamente desde este link: http://pueblista-pgpi.onrender.com**

---

##  Características

**A nivel organizacional**, para este proyecto hemos seguido las guías de planificaición enunciadas por el **PMBOK**. Nuestro proyecto fue desarrollado a lo largo de dos meses divididos en cuatro fases: inicio, planificación, ejecución y cierre. Los documentos de planificación referentes a este desarrollo se podrán encontrar en la carpeta ```/docs´´´ en la raíz de este proyecto. El desarrollo se ha llevado a cabo haciendo uso de la **metodología ágil Sprint**, siguiendo un ciclo de vida iterativo en cada Sprint.

**A nivel técnico**, este proyecto se ha realizado usando como base el framework de **Django**, haciendo uso de la arquitecura **model-view-template**. Los lenguages usandos han sido **Python**, HTML, CSS y JavaScript principalmente. Para las pruebas, se ha usado la librería **Pytest** para testear los módulos del proyecto. Más adelante, se detallan más en profundidad todos estos aspectos para poder probar tú mismo este proyecto.


##  Estructura del proyecto

```sh
└── pueblista-pgpi.git/
    ├── docs/
    │   ├── ...
    ├── plantilla-markdown/
    │   ├── ...
    ├── pueblista/
    │   ├── gestion_contactos/...
    │   ├── gestion_espacios/...
    │   ├── gestion_notificaciones/...
    │   ├── gestion_reservas/...
    │   ├── gestion_sms/...
    │   ├── gestion_usuarios/...
    │   ├── home/...
    │   ├── listado_reservas/...
    │   ├── pueblista/...
    │   ├── static/...
    │   ├── manage.py
    │   ├── locustfile.py
    │   └── templates/...
    ├── templates/
    ├── requirements.txt
    ├── README.md

```


###  Índice del proyecto
<details open>
        <summary><b>pueblista</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/locustfile.py'>locustfile.py</a></b></td>
                <td>- Locustfile.py define una prueba de carga para el sitio web<br>- Simula el comportamiento del usuario, específicamente cargando la página de inicio, para evaluar el rendimiento del sitio web bajo estrés<br>- El script utiliza el framework Locust para generar usuarios virtuales con tiempos de espera variables, proporcionando métricas de rendimiento para el análisis de escalabilidad y estabilidad<br>- Esto contribuye al proceso general de aseguramiento de la calidad del proyecto.</td>     </tr>
            <tr>
                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/manage.py'>manage.py</a></b></td>
                <td>- `manage.py` sirve como la interfaz principal de línea de comandos para el proyecto Pueblista basado en Django<br>- Proporciona el punto de entrada para ejecutar varias tareas administrativas, como ejecutar el servidor de desarrollo, migrar bases de datos y gestionar aplicaciones de Django<br>- Esencialmente, actúa como el punto de control central para interactuar con la infraestructura backend del proyecto.</td>     </tr>
            </table>
            <details>
                <summary><b>home</b></summary>
                <blockquote>
                    Este módulo contiene las plantillas de la página principal de la aplicación, además de las urls necearias para acceder a la navegación del resto del proyecto.
                    <table>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/home/models.py'>models.py</a></b></td>
                        <td><code>❯ ...</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/home/apps.py'>apps.py</a></b></td>
                        <td><code>❯ ...</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/home/admin.py'>admin.py</a></b></td>
                        <td><code>❯ ...</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/home/tests.py'>tests.py</a></b></td>
                        <td><code>❯ Pruebas unitarias en Pytest para el módulo. </code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/home/urls.py'>urls.py</a></b></td>
                        <td><code>❯ ...</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/home/views.py'>views.py</a></b></td>
                        <td><code>❯ ...</code></td>
                    </tr>
                    </table>
                    <details>
                        <summary><b>templates</b></summary>
                        <blockquote>
                            <table>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/home/templates/home.html'>home.html</a></b></td>
                                <td><code>❯ Esta es la plantilla que contiene la pantalla de frontend de la página principal.</code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/home/templates/editar_ayuntamiento.html'>editar_ayuntamiento.html</a></b></td>
                                <td><code>❯ Esta es la plantilla que contienen el formulario de edición del carusel de información del ayuntamiento.</code></td>
                            </tr>
                            </table>
                        </blockquote>
                    </details>
                </blockquote>
            </details>
            <details>
                <summary><b>gestion_notificaciones</b></summary>
                <blockquote>
                    Este módulo Permite a los administradores gestionar e interactuar con las notificaciones dentro del sistema de gestión de notificaciones de la aplicación `pueblista`<br> Esto simplifica la administración al proporcionar información de forma rápida a los usuarios de la aplicación.
                    <table>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_notificaciones/models.py'>models.py</a></b></td>
                        <td><code>❯ Modelo de datos del objeto `Notificación.`</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_notificaciones/apps.py'>apps.py</a></b></td>
                        <td><code>❯ ...</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_notificaciones/admin.py'>admin.py</a></b></td>
                        <td>El archivo `admin.py` integra el modelo `Notificacion` en la interfaz de administración de Django</td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_notificaciones/tests.py'>tests.py</a></b></td>
                        <td><code>❯ Pruebas unitarias en Pytest para el módulo. </code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_notificaciones/urls.py'>urls.py</a></b></td>
                        <td><code>❯ Direcciones para acceder a las notificaciones, marcarlas como leídas o cancelarlas. </code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_notificaciones/views.py'>views.py</a></b></td>
                        <td><code>❯ ... </code></td>
                    </tr>
                    </table>
                    <details>
                        <summary><b>templates</b></summary>
                        <blockquote>
                            <table>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_notificaciones/templates/notificaciones.html'>notificaciones.html</a></b></td>
                                <td><code>❯ Pantalla de visualización y gestión de las notificaciones. </code></td>
                            </tr>
                            </table>
                        </blockquote>
                    </details>
                </blockquote>
            </details>
            <details>
                <summary><b>gestion_espacios</b></summary>
                <blockquote>
                    <table>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_espacios/models.py'>models.py</a></b></td>
                        <td><code>❯ Se definen el modelo de EspacioPublico</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_espacios/apps.py'>apps.py</a></b></td>
                        <td><code>❯ ...</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_espacios/forms.py'>forms.py</a></b></td>
                        <td><code>❯ Formuñario de creacion y edición de un espacio y la actualización del estado de una reserva.</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_espacios/admin.py'>admin.py</a></b></td>
                        <td><code>❯ El archivo `admin.py` integra el modelo `EspacioPublico` en la interfaz de administración de Django</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_espacios/tests.py'>tests.py</a></b></td>
                        <td><code>❯ Pruebas unitarias en Pytest para el módulo. </code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_espacios/urls.py'>urls.py</a></b></td>
                        <td><code>❯ Direcciones para listar, crear, editar y elimiar espacios, y para mostrar las reservas de un espacio específico.</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_espacios/views.py'>views.py</a></b></td>
                        <td><code>❯ Vistas para la edición, listado, creación de espacios y vista de las reserva de cada espacio por separado. </code></td>
                    </tr>
                    </table>
                    <details>
                        <summary><b>templates</b></summary>
                        <blockquote>
                            <table>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_espacios/templates/list.html'>list.html</a></b></td>
                                <td><code>❯ Pantalla con el listado de todos lo espacios, para los administradores y para los usuaios por separado. </code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_espacios/templates/reservas.html'>reservas.html</a></b></td>
                                <td><code>❯ Pantalla que permite a los administradores ver y gestionar el estado de las reserva de cada espacio. </code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_espacios/templates/create.html'>create.html</a></b></td>
                                <td><code>❯ Pantalla de creación de un espacio. </code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_espacios/templates/edit.html'>edit.html</a></b></td>
                                <td><code>❯ Pantalla de edición de un espacio. </code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_espacios/templates/delete.html'>delete.html</a></b></td>
                                <td><code>❯ ... </code></td>
                            </tr>
                            </table>
                        </blockquote>
                    </details>
                </blockquote>
            </details>
            <details>
                <summary><b>pueblista</b></summary>
                <blockquote>
                    <table>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/pueblista/asgi.py'>asgi.py</a></b></td>
                        <td><code>❯ Archivo de configuración para la interfaz de servidor de aplicaciones asíncronas (ASGI) de Django.</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/pueblista/settings.py'>settings.py</a></b></td>
                        <td><code>❯ Archivo de configuración principal de Django, contiene todas las configuraciones globales del proyecto.</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/pueblista/urls.py'>urls.py</a></b></td>
                        <td><code>❯ Archivo de configuración de las rutas URL del proyecto a nivel general, define cómo se mapean las URLs a las vistas.</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/pueblista/wsgi.py'>wsgi.py</a></b></td>
                        <td><code>❯ Archivo de configuración para la interfaz de servidor de aplicaciones web (WSGI) de Django.</code></td>
                    </tr>
                    </tr>
                    </table>
                </blockquote>
            </details>
            <details>
                <summary><b>gestion_reservas</b></summary>
                <blockquote>
                    <table>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_reservas/models.py'>models.py</a></b></td>
                        <td><code>❯ Se definen los modelos de datos para los objetos `Reserva`y `SolicitudReservaEspecial`.</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_reservas/apps.py'>apps.py</a></b></td>
                        <td><code>❯ ... </code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_reservas/forms.py'>forms.py</a></b></td>
                        <td><code>❯ Formularios para la pertición de reservas especiales.</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_reservas/admin.py'>admin.py</a></b></td>
                        <td><code>❯ El archivo `admin.py` integra el modelo `Reserva` en la interfaz de administración de Django.</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_reservas/tests.py'>tests.py</a></b></td>
                        <td><code>❯ Pruebas unitarias en Pytest para el módulo. </code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_reservas/urls.py'>urls.py</a></b></td>
                        <td><code>❯ Direcciones para crear, cancelar, aceptar, ver solicitudes por espacio, ver solicitudes pendientes y ver todas las solicitudes de cada usuario. </code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_reservas/views.py'>views.py</a></b></td>
                        <td><code>❯ ...</code></td>
                    </tr>
                    </table>
                    <details>
                        <summary><b>templates</b></summary>
                        <blockquote>
                            <table>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_reservas/templates/solicitud_reserva_especial.html'>solicitud_reserva_especial.html</a></b></td>
                                <td><code>❯ Vista del formulario de solicitud de una reservas especial. </code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_reservas/templates/calendario_reservas.html'>calendario_reservas.html</a></b></td>
                                <td><code>❯ Vista del calendario de reservas de una reserva. En esta pantalla el usuario puede seleccionar las horas en las que realizar una reserva de un espacio, además de cancelarlas si lo deseara. </code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_reservas/templates/solicitudes_pendientes.html'>solicitudes_pendientes.html</a></b></td>
                                <td><code>❯ Pantalla en la que los administradores podrán consultar las solicitudes pendientes. </code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_reservas/templates/mis_solicitudes.html'>mis_solicitudes.html</a></b></td>
                                <td><code>❯ Pantalla en la que un usuario podrá ver un historial de sus solicitudes. </code></td>
                            </tr>
                            </table>
                        </blockquote>
                    </details>
                </blockquote>
            </details>
            <details>
                <summary><b>gestion_usuarios</b></summary>
                <blockquote>
                    <table>
                        <tr>
                            <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_usuarios/models.py'>models.py</a></b></td>
                            <td><code>❯ Se definen los modelos de datos para los objetos `CustomUser` y `CustomUserManager`.</code></td>
                        </tr>
                        <tr>
                            <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_usuarios/apps.py'>apps.py</a></b></td>
                            <td><code>❯ ...</code></td>
                        </tr>
                        <tr>
                            <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_usuarios/forms.py'>forms.py</a></b></td>
                            <td><code>❯ Formularios para inicio de sesión de usuarios.</code></td>
                        </tr>
                        <tr>
                            <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_usuarios/backends.py'>backends.py</a></b></td>
                            <td><code>❯ Backend de autenticación personalizado para el modelo `CustomUser`.</code></td>
                        </tr>
                        <tr>
                            <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_usuarios/admin.py'>admin.py</a></b></td>
                            <td><code>❯ El archivo `admin.py` integra el modelo `CustomUser` en la interfaz de administración de Django.</code></td>
                        </tr>
                        <tr>
                            <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_usuarios/tests.py'>tests.py</a></b></td>
                            <td><code>❯ Pruebas unitarias en Pytest para el módulo.</code></td>
                        </tr>
                        <tr>
                            <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_usuarios/urls.py'>urls.py</a></b></td>
                            <td><code>❯ Direcciones para el registro, inicio de sesión, perfil de usuario y listado de usuarios.</code></td>
                        </tr>
                        <tr>
                            <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_usuarios/views.py'>views.py</a></b></td>
                            <td><code>❯ Vistas para el registro, inicio de sesión, perfil de usuario y listado de usuarios.</code></td>
                        </tr>
                        <tr>
                            <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_usuarios/decorators.py'>decorators.py</a></b></td>
                            <td><code>❯ Decoradores personalizados para la gestión de permisos y autenticación.</code></td>
                        </tr>
                    </table>
                    <details>
                        <summary><b>templates</b></summary>
                        <blockquote>
                            <table>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_usuarios/templates/login.html'>login.html</a></b></td>
                                <td><code>❯ Plantilla para la pantalla de inicio de sesión.</code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_usuarios/templates/perfil.html'>perfil.html</a></b></td>
                                <td><code>❯ Plantilla para la pantalla de perfil de usuario.</code></td>
                            </tr>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/gestion_usuarios/templates/user_list.html'>user_list.html</a></b></td>
                                <td><code>❯ Plantilla para la pantalla de listado de usuarios (solo para administradores).</code></td>
                            </tr>
                            </table>
                        </blockquote>
                    </details>
            </details>
            <details>
                <summary><b>listado_reservas</b></summary>
                <blockquote>
                    <table>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/listado_reservas/models.py'>models.py</a></b></td>
                        <td><code>❯ ... </code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/listado_reservas/apps.py'>apps.py</a></b></td>
                        <td><code>❯ ... </code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/listado_reservas/admin.py'>admin.py</a></b></td>
                        <td><code>❯ Integración del modelo `ListadoReservas` en la interfaz de administración de Django.</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/listado_reservas/tests.py'>tests.py</a></b></td>
                        <td><code>❯ Pruebas unitarias en Pytest para el módulo.</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/listado_reservas/urls.py'>urls.py</a></b></td>
                        <td><code>❯ Direcciones para acceder al listado de reservas de un usuario y cancelar reservas.</code></td>
                    </tr>
                    <tr>
                        <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/listado_reservas/views.py'>views.py</a></b></td>
                        <td><code>❯ Vistas para mostrar y gestionar el listado de reservas de un usuario.</code></td>
                    </tr>
                    </table>
                    <details>
                        <summary><b>templates</b></summary>
                        <blockquote>
                            <table>
                            <tr>
                                <td><b><a href='https://github.com/Pueblista-PGPI/pueblista-pgpi.git/blob/master/pueblista/listado_reservas/templates/listado_reservas.html'>listado_reservas.html</a></b></td>
                                <td><code>❯ Pantalla que incluye el listado de las reservas de un usuario y permite su cancelación.</code></td>
                            </tr>
                            </table>
                        </blockquote>
                    </details>
                </blockquote>
            </details>
                    </tr>
                    </table>
                </blockquote>
            </details>
        </blockquote>
</details>

---


##  Empezando

###  Prerrequisitos
Antes de comenzar con pueblista-pgpi.git, asegúrate de que tu entorno de ejecución cumpla con los siguientes requisitos:

- **Lenguaje de programación:** Python 3.12 o superior
- **Gestor de paquetes:** Pip / Pip3 o superior


###  Instalación
Instala pueblista-pgpi.git usando uno de los siguientes métodos:

**Construir desde el código fuente:**

1. Clona el repositorio pueblista-pgpi.git:
```sh
❯ git clone https://github.com/Pueblista-PGPI/pueblista-pgpi.git
```

2. Navega al directorio del proyecto:
```sh
❯ cd pueblista-pgpi.git
```

3. Crear un entorno virtual en el directorio raíz del proyecto:
```sh
❯ python -m venv env
```

4. Activa el entorno virtual:

**En Windows:**
```sh
❯ .\env\Scripts\activate
```

**En macOS y Linux:**
```sh
❯ source env/bin/activate
```

5. Instala las dependencias del proyecto:
```sh
❯ pip install -r requirements.txt
```

**Nota**: En caso de usar MacOS, se tendrá que usar `pip3` en lugar que pip a la hora de instalar el archivo *requirements*.

6. Sustituye el archivo `env.example` completando con los tus datos y cambia el nombre a `.env`.

7. Instala PostgresSQL:

**En Windows:**
```sh
❯ choco install postgresql
```

**En macOS:**
```sh
❯ brew install postgresql
```

**En Linux:**
```sh
❯ sudo apt-get install postgresql postgresql-contrib
```

8. Inicia el servicio de PostgreSQL:

**En Windows:**
```sh
❯ net start postgresql
```

**En macOS:**
```sh
❯ brew services start postgresql
```

**En Linux:**
```sh
❯ sudo service postgresql start
```

9. Crea una base de datos y un usuario para el proyecto:

```sh
❯ sudo -u postgres psql
postgres=# CREATE DATABASE pueblista;
postgres=# CREATE USER pueblista_user WITH ENCRYPTED PASSWORD 'tu_contraseña';
postgres=# GRANT ALL PRIVILEGES ON DATABASE pueblista TO pueblista_user;
postgres=# \q
```

10. Configura las variables de entorno en el archivo `.env` con los datos de la base de datos:

```sh
DATABASE_NAME=pueblista
DATABASE_USER=pueblista_user
DATABASE_PASSWORD=tu_contraseña
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

###  Uso
Ejecuta pueblista-pgpi.git siguiendo estos:
**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

1. Muévete al directorio pueblista

```sh
❯ cd pueblista
```

2. Crea las migraciones
```sh
❯ python manage.py makemigrations
❯ python manage.py migrate
```

3. Ejecuta el proyecto
```sh
❯ python manage.py runserver
```

4. Tras esto, solo hay que meter la siguiente url en el navegador, y así tendríamos desplegado el proyecto de forma local: http://localhost:5000

###  Pruebas
Ejecuta la suite de pruebas usando el siguiente comando (Nota: para esto se deben haber seguido antes las instrucciones de uso, principalemtne, instalando el archivo requirements.txt):
**Usando `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```

Para comprobar la cobertura de código (*coverage*) de la siute de pruebas, ejecuta el siguiente comando:

```sh
❯ coverage run --source=<tu_modulo> manage.py test <tu_modulo>
```

donde `tu_modulo` es el nombre del módulo a testear entre los siguientes: `gestion_espacios`, `gestion_notificaciones`, `gestion_reservas`, `gestion_usuarios`, `home` y `listado_reservas`.
   
Ejecutar `coverage report -m` para ver el reporte de cobertura en la terminal.
   
Ejecutar `coverage html` para generar el reporte de cobertura en un archivo HTML `htmlcov/index.html`

---

##  Licencia

Este proyecto está protegido bajo la licencia básica MIT. Para más detalles, consulte el archivo [LICENSE](https://choosealicense.com/licenses/mit/).


---

## Autores

A continuación se listan los autores del proyecto en orden alfabético:

<table>
    <tr>
        <td align="center">
            <a href="https://github.com/josemicpy">
                <img src="https://avatars.githubusercontent.com/u/62075385?v=4" width="100px;" alt="José Miguel Iborra"/>
                <br />
                <sub><b>José Miguel Iborra</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/rgavira123">
                <img src="https://avatars.githubusercontent.com/u/91947011?v=4" width="100px;" alt="Ramón Gavira"/>
                <br />
                <sub><b>Ramón Gavira</b></sub>
            </a>
        </td>
                <td align="center">
            <a href="https://github.com/DaniFdezCab">
                <img src="https://avatars.githubusercontent.com/u/92794081?v=4" width="100px;" alt="Daniel Fernández"/>
                <br />
                <sub><b>Daniel Fernández</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/antoniommff">
                <img src="https://avatars.githubusercontent.com/u/91947070?v=4" width="100px;" alt="Antonio Macías"/>
                <br />
                <sub><b>Antonio Macías</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/rafpulcif">
                <img src="https://avatars.githubusercontent.com/u/91948036?v=4" width="100px;" alt="Rafael Pulido"/>
                <br />
                <sub><b>Rafael Pulido</b></sub>
            </a>
        </td>
    </tr>
</table>

---

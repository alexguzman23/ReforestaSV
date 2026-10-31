# REFORESTASV

## Integrantes
* Pedro Alexander Henríquez Guzmán
* Jared Emanuel Marín Rodríguez
* Cesar Oliver Salazar Mejía
* Brayan Adonay Peñate Alas
* Eduard Francisco Peraza Guardado
* Wendy Zelena Peraza Guevara

## Descripción Inicial de la Problemática
La problemática central que busca resolver **REFORESTASV** es la falta de seguimiento y control posterior a la ejecución de las campañas de reforestación. 
En la actualidad, muchas iniciativas se limitan únicamente a la siembra inicial de árboles, descuidando el monitoreo constante requerido para garantizar su supervivencia.

Esto genera una pérdida significativa de recursos e impacto ambiental, ya que no existe un registro organizado sobre quién es el responsable de cada árbol, 
su ubicación exacta, las labores de riego o mantenimiento aplicadas, ni el estado de salud real de los ejemplares (si continúan activos, si han sido dañados
o si se han perdido). La falta de herramientas de inventario e identificación por especie impide una gestión eficiente y la toma de decisiones informadas
para proteger el ecosistema reforestado. 

## Beneficiarios
El proyecto está dirigido principalmente a la Asociación Ecológica EcoRaíces, ubicada en Chalatenango Centro, Chalatenango.

También podrán beneficiarse:
- Voluntarios y brigadas de reforestación.
- Estudiantes y miembros de la comunidad.
- Coordinadores de proyectos ambientales.
- Instituciones que desarrollen actividades de reforestación.

## Requisitos funcionales

1. El sistema permitirá autenticar a los usuarios mediante usuario y contraseña.
2. El sistema permitirá crear y administrar campañas de reforestación.
3. El sistema permitirá registrar el inventario de árboles.
4. El sistema permitirá registrar y visualizar la ubicación de los árboles.
5. El sistema permitirá programar y consultar calendarios de riego.
6. El sistema permitirá actualizar el estado de salud de los árboles.
7. El sistema permitirá registrar evidencias de mantenimiento.
8. El sistema mostrará un resumen estadístico de supervivencia de los árboles.

## Requisitos no funcionales

1. La interfaz deberá adaptarse a computadoras y dispositivos móviles.
2. Los formularios deberán validar los campos obligatorios antes de guardar la información.
3. El sistema deberá proteger el acceso mediante un inicio de sesión con usuario y contraseña, evitando el acceso de personas no autorizadas.
4. El sistema deberá utilizar SQL Server como gestor de base de datos.
5. La aplicación deberá desarrollarse con Django, un framework de Python, para construir y organizar las funciones principales del sistema.

## Clase Principal del Sistema

1. CampañaReforestación: Administra los datos generales de las campañas, fechas y la institución beneficiaria.
2. Árbol: Controla el inventario individual, código único, fecha de plantación y estado de salud actual.
3. Especie: Almacena el catálogo de especies nativas y sus requerimientos de riego.
4. Ubicación: Registra las coordenadas geográficas (latitud y longitud) y zonas de referencia.
5. Responsable: Administra los roles y la asignación del personal de campo.
6. Mantenimiento: Registra las actividades de riego, podas, comentarios y evidencias fotográficas.
7. Usuario: Gestiona la autenticación y los permisos de acceso mediante el sistema de Django.

## Instrucciones básicas para instalar y ejecutar la aplicación

Para ejecutar ReforestaSV en un entorno local, es necesario tener instalados Python, SQL Server y el controlador ODBC para SQL Server.

### 1. Clonar el repositorio

```bash
git clone https://github.com/alexguzman23/ReforestaSV.git
cd ReforestaSV
```

### 2. Crear y activar el entorno virtual

En la terminal de Visual Studio Code, ejecutar:

```powershell
py -m venv env
```

Activar el entorno virtual en Windows:

```powershell
.\env\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

Instalar las librerías necesarias utilizando el archivo `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

### 4. Configurar SQL Server

Crear una base de datos en SQL Server con el nombre:

`reforestasv_bd`

En la carpeta principal del proyecto, donde se encuentra `manage.py`, crear un archivo llamado `.env` con la siguiente configuración de ejemplo:

```dotenv
DB_NAME=reforestasv_bd
DB_HOST=localhost
DB_DRIVER=ODBC Driver 17 for SQL Server
DB_TRUSTED_CONNECTION=yes
```

Los valores deben ajustarse a la configuración de SQL Server de cada integrante. El archivo `.env` no debe subirse al repositorio por seguridad.

### 5. Verificar la configuración

Ejecutar el siguiente comando:

```powershell
python manage.py check
```

Si no existen errores, Django mostrará un mensaje indicando que la comprobación fue satisfactoria.

### 6. Ejecutar la aplicación

Iniciar el servidor de desarrollo de Django:

```powershell
python manage.py runserver
```

Abrir en el navegador la siguiente dirección:

http://127.0.0.1:8000/

Actualmente, la aplicación muestra una página básica de bienvenida a ReforestaSV, como comprobación del funcionamiento del servidor.

**Nota:** Durante la Semana 4 se creó la estructura inicial del proyecto, se definieron las clases principales y se comprobó la conexión con SQL Server.


## Semana 5: Implementación de Modelos y Base de Datos

Durante esta semana se implementaron las clases principales del sistema como modelos de Django, estableciendo sus relaciones y creando las tablas correspondientes en SQL Server.

### 1. Reestructuración de la Arquitectura
* **Migración por funcionalidades:** Se reorganizó la estructura del proyecto de manera modular, separando las aplicaciones según su función (ej. `Gestion_Arboles` y `CampanaReforestacion`) y eliminando las carpetas obsoletas.
* **Integración de Usuarios:** Se creó la aplicación `usuarios` para gestionar perfiles, roles y permisos, vinculándola con el sistema de autenticación de Django a través de `AUTH_USER_MODEL`.

### 2. Creación y Definición de Modelos (POO)
* Se desarrollaron las clases principales heredando de `models.Model`, definiendo los atributos con los tipos de datos apropiados.
* Se implementó el método `__str__()` en cada modelo para facilitar su visualización y se añadieron métodos propios para definir el comportamiento de las entidades.
* Se establecieron las relaciones entre los modelos (utilizando campos como `ForeignKey`) para conectar la información de las distintas aplicaciones.

### 3. Migraciones en SQL Server
* Se verificó la integridad del sistema mediante el comando `python manage.py check`, comprobando que no existieran errores de configuración.
* Se ejecutó `python manage.py makemigrations` para preparar los archivos de migración de las aplicaciones `CampanaReforestacion`, `Gestion_Arboles` y `Usuarios`.
* Se crearon las tablas físicas en la base de datos `reforestasv_bd` de SQL Server aplicando el comando `python manage.py migrate`.

### 4. Datos de Prueba y Panel Administrativo
* Se creó un superusuario (ej. `adonay`) desde la terminal utilizando `python manage.py createsuperuser`.
* Se registraron los modelos en el panel administrativo de Django (`http://127.0.0.1:8000/admin`) y se ingresaron datos de prueba reales para el sistema:
  * **Campañas:** Reforestación Chalatenango 2026.
  * **Especies:** Registro de catálogo (ej. Maquilishuat).
 
  * ## Semana 6: Implementación del CRUD, Autenticación y Diseño de Interfaz

Durante esta semana se desarrollaron nuevas funcionalidades para ReforestaSV, permitiendo administrar los árboles registrados, controlar el acceso de los usuarios y mejorar la presentación visual del sistema.

### 1. Implementación del CRUD de Árboles

- Se implementaron las operaciones de crear, consultar, editar y eliminar árboles mediante las vistas `arbol_create`, `arbol_list`, `arbol_update` y `arbol_delete`.
- Se utilizaron formularios de Django (`ArbolForm`) para validar y almacenar la información.
- Se configuraron las rutas correspondientes en `urls.py` para acceder a cada operación.
- Se incorporaron plantillas HTML para mostrar el inventario y gestionar los registros.

### 2. Autenticación y Seguridad

- Se implementó el registro de usuarios mediante `UserCreationForm`.
- Se configuraron las funciones de inicio y cierre de sesión utilizando `LoginView` y `LogoutView`.
- Se protegieron las vistas mediante `@login_required`, restringiendo el acceso a usuarios no autenticados.
- Se configuraron las redirecciones de inicio y cierre de sesión en `settings.py`.

### 3. Diseño de Interfaz y Archivos Estáticos

- Se personalizó la plantilla `base.html` utilizando Bootstrap 5 y Bootstrap Icons.
- Se incorporó una barra de navegación con identificación del usuario y opción para cerrar sesión.
- Se integraron notificaciones mediante `django.contrib.messages`.
- Se creó el archivo `reforestasv.css` para personalizar los estilos de la aplicación y se corrigieron problemas relacionados con su carga.

### 4. Control de Versiones y Pruebas

- Se registraron los avances mediante commits en Git y se sincronizaron los cambios con el repositorio de GitHub.
- Se verificó el funcionamiento del inventario, los formularios CRUD, la autenticación y la navegación.
- Se comprobó la correcta aplicación de los estilos y componentes visuales.

Con estas mejoras, ReforestaSV pasó de contar únicamente con una estructura inicial de modelos y base de datos a disponer de funcionalidades de administración de árboles, autenticación de usuarios e interfaces para la gestión de información.
  * **Responsables:** Asignación de roles como "Encargado de campo".
  * **Mantenimiento y Árboles:** Registro de inventario y evidencias de mantenimiento (ej. riegos de prueba).

### 5. Control de Versiones
* Se prepararon los cambios y se ejecutó `git pull` para sincronizar el repositorio local con los avances del equipo.
* Se enviaron los cambios consolidados a la rama `main` mediante `git push`, manteniendo actualizado el historial de commits con las responsabilidades de cada integrante.

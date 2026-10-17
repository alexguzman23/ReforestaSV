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
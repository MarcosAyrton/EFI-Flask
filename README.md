# EFI FLASK parte 1:
Esta guía te ayudará a configurar y ejecutar nuestra aplicación Flask utilizando Python, Flask, SQLAlchemy, Flask-Migrate y PyMySQL. 
Además, incluye pasos para la instalación de XAMPP, que nos proporcionará un servidor web local con MySQL.

# Clonación del Repositorio desde GitHub
1. Instala Git:
   * Ubuntu: 'sudo apt install git'

2. Crea un directorio para el proyecto:
   * mkdir nombre_del_directorio
   * cd nombre_del_directorio

3. Clona el repositorio en el directorio creado:
   * Ejecuta el siguiente comando: git clone https://github.com/usuario/nombre_del_repositorio.git
   * Reemplaza 'usuario' y 'nombre_del_repositorio' con los valores correctos de tu repositorio.

4. Accede al directorio del proyecto:
   * cd nombre_del_repositorio

#  Instalación de Python y Entorno Virtual
1. Actualiza el sistema:
   * sudo apt update

2. Instala Python 3 y pip:
   * sudo apt install python3 python3-pip

3. Crea un entorno virtual:
   * python3 -m venv env

4. Activa el entorno virtual:
   * source env/bin/activate

5. Instala Flask y las dependencias necesarias:
   * pip install Flask Flask-SQLAlchemy Flask-Migrate PyMySQL

#  Instalación y Configuración de XAMPP
1. Descarga XAMPP:
   * Ve a la página oficial de XAMPP y descarga la versión para Linux

2. Da permisos de ejecución al instalador:
   * chmod +x xampp-linux-x64-*.run

3. Instala XAMPP:
   * sudo ./xampp-linux-x64-*.run

4. Inicia XAMPP:
   * sudo /opt/lampp/lampp start

5. Configura la base de datos:
   * Abre 'http://localhost' en tu navegador.
   * Accede a phpMyAdmin y crea una nueva base de datos llamada 'Tomastemarc_Cell_DB'

# Configuración y Ejecución de Migraciones
1. Inicializa las migraciones:
   * flask db init

2. Genera una migración:
   * flask db migrate -m "Initial migration"

3. Aplica la migración a la base de datos:
   * flask db upgrade

4. Ejecuta la Aplicación Flask:
   * Abre el directorio del proyecto en tu editor de código favorito.
   * Activa el entorno virtual si no lo has hecho: source env/bin/activate
   * Inicia la aplicación Flask: flask run --reload


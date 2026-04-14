# SeguriComunidad

Proyecto integrador para el cuatrimestre: **Seguridad Vecinal y Atención de Emergencias**.

**Tecnologías utilizadas:**
- Flutter 3.24.0 (App móvil)
- FastAPI + Python 3.13.7 (Backend orientado a servicios - REST API)
- PostgreSQL 18.3 (Base de datos avanzada con triggers y stored procedures)
- Ubuntu 25.10

**Materias cubiertas:**
- Aplicaciones Web Orientadas a Servicios
- Bases de Datos Avanzadas
- Estándares y Métricas para el Desarrollo de Software

Desarrollado como preparación para estancias y perfil Junior Dev.

## Estructura del proyecto
- `/backend` → API con FastAPI
- `/frontend` → App Flutter
- `/database` → Scripts SQL, diagramas ER
- `/docs` → Documentación, estándares ISO, métricas

## Instalación y ejecución
Para los primeros pasos, es necesario activar el entorno virtual para poder trabajar en el proyecto.
Paro eso, hay que hacer lo siguiente:
Como primer paso debemos crear el entorno virtual, en este caso 'venv' con el siguiente comando en la terminal:
- python3 -m venv venv
Posteriormente debemos activar el entorno con el siguiente comando:
- source venv/bin/activate
De esta manera ya podemos hacer cambios en el backend sin ninguna complicación. Además poder instalar nuevas librerias sin afectar todo el proyecto.
Para poder salir del entorno virtual y modificar otra parte del proyecto es con el comando:
- deactivate
Otro de los comandos que se utilizan durante el proyecto es el comando 'pip' el cual nos permite instalar librerias y paquetes nuevos, su sintaxis es la siguiente:
- pip install nombre_paquete
Para crear un archivo donde guardar las dependencias que utiliazará el proyecto se utiliza el siguiente comando:
- pip freeze > requeriments.txt


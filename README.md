# Sistema para administración de empleados

## Comenzando 🚀

_Este simple sistema para la administración de empleados permite, agregar nuevos empleados a la lista con sus respectivos datos (Nombre, correo, foto y el sistema le asigna un id), tambien permite editar y eliminar dicha información._

### Pre-requisitos 📋

1. Python 3.7.3
2. XAMPP


### Instalación 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

1. Descargar el proyecto
2. Iniciar Apache y MySql en XAMPP
3. Entra a phpmyadmin en tu navegador, luego busca la opción de crear nueva base de datos la cual llevara por nombre "sistema" dentro de ella vas a crear una nueva tabla con 4 columnas las cuales van en el siguiente orden y su respectivo tipo de varible :
* "id" int(10) - Marcar id como llave primaria y activar la casilla A_I (AUTO_INCREMENT)
* "nombre" varchar(255)
* "correo" varchar(255)
* "foto" varchar(5000)

Nota: Colocar el nombre de la base de datos y de las columnas igual a los ejemplos.

4. Intalación de paquetes necesarios:

```
pip install flask
pip install Flask-MySQL
pip install jinja2
```
5. En la carpeta principal del proyecto crea una nueva carpeta llamada "uploads" que es donde se guardaran las fotos de los empleados.

6. Ejecutar la aplicación

```
python app.py
```

## Construido con 🛠️

* [Python 3.7.3](https://www.python.org/downloads/release/python-370/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Flask-MySQL](https://flask-mysql.readthedocs.io/en/stable/)
* [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/)

## Autor ✒️

* [isaacv4071](https://github.com/isaacv4071)

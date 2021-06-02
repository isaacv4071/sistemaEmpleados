#importaciones
from flask import Flask
from flask import render_template,request,redirect,url_for,flash
from flaskext.mysql import MySQL
from flask import send_from_directory
from datetime import datetime
import os

from pymysql import cursors 


app = Flask(__name__) #se crea la aplicación
app.secret_key="developed"

mysql = MySQL()
#uso de mysql y conexion con los datos
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema'
mysql.init_app(app)

CARPETA=os.path.join('uploads')
app.config['CARPETA']=CARPETA

@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'], nombreFoto)

#ruta principal
@app.route('/')
def index():
    sql="SELECT * FROM `empleados`;"
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    empleados = cursor.fetchall()
    conn.commit()
    return render_template('empleados/index.html', empleados=empleados)

#borrar empleado por id
@app.route('/destroy/<int:id>')
def destroy(id):
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT foto FROM empleados WHERE id=%s", id)
    fila=cursor.fetchall()
    os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
    cursor.execute("DELETE FROM empleados WHERE id=%s",(id))#borrar empleado
    conn.commit()
    return redirect('/')

#ruta para editar por id de empleado
@app.route('/edit/<int:id>')
def edit(id):
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM empleados WHERE id=%s",(id))
    empleados = cursor.fetchall()
    conn.commit()
    return render_template('empleados/edit.html', empleados=empleados)

#rcapturar los datos y actulizarlos 
@app.route('/update', methods=['POST'])
def update():
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']
    id=request.form['txtID']
    sql="UPDATE empleados SET nombre=%s, correo=%s WHERE id=%s;" #actualizar nombre y correo
    datos = (_nombre,_correo,id)
    conn = mysql.connect()
    cursor=conn.cursor()
    now=datetime.now() #capturar el tiempo actual del sistema
    tiempo=now.strftime("%Y%H%M%S") #formato del tiempo
    if _foto.filename !='':
        nuevoNombreFoto=tiempo+_foto.filename #se da el nuevo nombre de la foto
        _foto.save('uploads/'+nuevoNombreFoto)
        cursor.execute("SELECT foto FROM empleados WHERE id=%s", id)
        fila=cursor.fetchall()
        os.remove(os.path.join(app.config['CARPETA'], fila[0][0]))
        cursor.execute("UPDATE empleados SET foto=%s WHERE id=%s",(nuevoNombreFoto,id))
        conn.commit()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')

#ruta para el registro de empleados
@app.route('/create')
def create():
    return render_template('empleados/create.html')

#ruta para recepcion de datos
@app.route('/store', methods=['POST'])
def storage():
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']

    if _nombre == '' or _correo == '' or  _foto == '':
        flash('Recuerda llenar los datos de los campos')
        return redirect((url_for('create')))

    now=datetime.now() #capturar el tiempo actual del sistema
    tiempo=now.strftime("%Y%H%M%S") #formato del tiempo
    if _foto.filename !='':
        nuevoNombreFoto=tiempo+_foto.filename #se da el nuevo nombre de la foto
        _foto.save('uploads/'+nuevoNombreFoto)
    sql="INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL,%s,%s,%s);" #insertar datos en la DB
    datos = (_nombre,_correo,nuevoNombreFoto)
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

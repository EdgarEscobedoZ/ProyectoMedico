from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MySQL_HOST']='localhost'
app.config['MySQL_USER']='root'
app.config['MySQL_PASSWORD']=''
app.config['MySQL_DB']='bdcentromedico'
app.secret_key='mysecretkey'
mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/registroMedico', methods=('POST'))
def registrarMedico():
    if request.method == 'POST':
        VRFC = request.form['RFC']
        VNOMBRE = request.form['nombre_completo']
        VCEDULA = request.form['cedula']
        VCORREO = request.form['correo']
        VCONTRASEÑA = request.form['contraseña']
        VROL = request.form['rol']
        print(VRFC, VNOMBRE, VCEDULA, VCORREO, VCONTRASEÑA, VROL)
    return 'Los datos llegaron correctamente'

@app.route('/registroPaciente', methods=('POST'))
def registrarMedico():
    if request.method == 'POST':
        VMEDICO = request.form['medico']
        VNOMBRE = request.form['nombre_completo']
        VFECHANAC = request.form['fecha_nacimiento']
        VENFERMEDAD = request.form['enfermedades_cronicas']
        VALERGIAS = request.form['alergias']
        VANTECEDENTES = request.form['antecedentes_familiares']
        print(VMEDICO, VNOMBRE, VFECHANAC, VENFERMEDAD, VALERGIAS, VANTECEDENTES)
    return 'Los datos llegaron correctamente'
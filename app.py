from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='bdcentromedico'
app.secret_key='mysecretkey'
mysql=MySQL(app)



@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/consulta_admin')
def consultaad():
    return render_template('MedicoAdmin/consulta_admin.html')

@app.route('/actualizacion_admin')
def actuadmin():
    return render_template('MedicoAdmin/actualizacion_admin.html')

@app.route('/eliminar_admin')
def eliminaradmin():
    return render_template('MedicoAdmin/eliminar_admin.html')

@app.route('/consultacita')
def consultacita():
    return render_template('Medico/consultacita.html')

@app.route('/consultapaciente')
def consultapaciente():
    return render_template('Medico/consultapaciente.html')



@app.route('/registro_admin')
def registro_admin():
    return render_template('MedicoAdmin/registro_admin.html')

@app.route("/registro_adminBD", methods=['POST'])
def registrarMedico():
    if request.method == 'POST':
        VRFC = request.form['RFC']
        VNOMBRE = request.form['Nombre']
        VCEDULA = request.form['cedula']
        VCORREO = request.form['correo']
        VCONTRASEÑA = request.form['contrasena']
        VROL = request.form['rol']

        cs = mysql.connection.cursor()
        cs.execute('INSERT INTO tb_medicos (rfc, nombre_completo, cedula, correo, contraseña, rol) VALUES (%s, %s, %s, %s, %s, %s)', (VRFC, VNOMBRE, VCEDULA, VCORREO, VCONTRASEÑA, VROL))
        mysql.connection.commit()

        
    return render_template('ventanaemergente.html')

@app.route('/expediente_paciente')
def expediente_paciente():
    return render_template('Medico/expediente_paciente.html')

@app.route("/expediente_pacienteBD", methods=['POST'])
def registrarPaciente():
    if request.method == 'POST':
        VMEDICO = request.form['medico']
        VNOMBRE = request.form['Nombre']
        VFECHANAC = request.form['fechanac']
        VENFERMEDAD = request.form['enfermedades']
        VALERGIAS = request.form['alergia']
        VANTECEDENTES = request.form['antecedentes']
        print(VMEDICO, VNOMBRE, VFECHANAC, VENFERMEDAD, VALERGIAS)


        cs = mysql.connection.cursor()
        #cs.execute('INSERT INTO tb_pacientes (medico, nombre_completo, fecha_nacimiento, enfermedades_cronicas, alergias) VALUES (%s, %s, %s, %s, %s)',(VMEDICO, VNOMBRE, VFECHANAC, VENFERMEDAD, VALERGIAS))
        cs.execute('INSERT INTO tb_pacientes (medico, nombre_completo, fecha_nacimiento, enfermedades_cronicas, alergias, antecendentes_familiares) VALUES (%s, %s, %s, %s, %s, %s)',(VMEDICO, VNOMBRE, VFECHANAC, VENFERMEDAD, VALERGIAS, VANTECEDENTES))
        mysql.connection.commit()


    return render_template('ventanaemergente.html')


#Ejecucion del servidor

if __name__ == '__main__':
    app.run(port=5000, debug=True)
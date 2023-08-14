from flask import Flask, render_template, request, redirect, url_for, flash, Response
from flask_mysqldb import MySQL
import subprocess

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

#   MEDICO ADMINISTRADOR    #

@app.route('/registro_admin')
def registro_admin():
    return render_template('MedicoAdmin/registro_admin.html')

@app.route("/registro_adminBD", methods=['POST'])
def registrarMedico():
    if request.method == 'POST':
        VRFC = request.form['RFC']
        VNOMBRE = request.form['nombrec']
        VCEDULA = request.form['cedula']
        VCORREO = request.form['correo']
        VCONTRASEÑA = request.form['contrasena']
        VROL = request.form['rol']

        cs = mysql.connection.cursor()
        cs.execute('INSERT INTO tb_medicos (rfc, nombre_completo, cedula, correo, contraseña, rol) VALUES (%s, %s, %s, %s, %s, %s)', (VRFC, VNOMBRE, VCEDULA, VCORREO, VCONTRASEÑA, VROL))
        mysql.connection.commit()
        

    flash('Mensaje')
    return redirect(url_for('registro_admin'))

@app.route('/consulta_admin')
def consulta_admin():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tb_medicos')
    data = cur.fetchall()
    return render_template('MedicoAdmin/consulta_admin.html', medicos = data)

@app.route('/actualizacion_admin/<id>')
def actuadmin(id):
    cs = mysql.connection.cursor()
    cs.execute('SELECT * FROM tb_medicos where id = %s', (id,))
    data = cs.fetchall()
    return render_template('MedicoAdmin/actualizacion_admin.html', Edicion = data)

@app.route('/actualizacion_adminBD/<id>', methods=['POST'])
def actuadminBD(id):
    if request.method == 'POST':
        VRFC = request.form['RFC']
        VNOMBRE = request.form['nombrec']
        VCEDULA = request.form['cedula']
        VCORREO = request.form['correo']
        VCONTRASEÑA = request.form['contrasena']
        VROL = request.form['rol']

        cs = mysql.connection.cursor()
        cs.execute('UPDATE tb_medicos SET rfc = %s, nombre_completo = %s, cedula = %s, correo = %s, contraseña = %s, rol = %s WHERE id = %s', (VRFC, VNOMBRE, VCEDULA, VCORREO, VCONTRASEÑA, VROL, id))
        mysql.connection.commit()
    
    flash('Mensaje')
    return redirect(url_for('consulta_admin'))

@app.route('/eliminar_admin/<id>')
def eliminaradmin(id):
    cs = mysql.connection.cursor()
    cs.execute('select * from tb_medicos where id = %s', (id,))
    data = cs.fetchall()
    return render_template('MedicoAdmin/eliminar_admin.html', Eliminar = data)

@app.route('/eliminar_adminBD/<id>', methods=['POST'])
def eliminaradminBD(id):
    if request.method == 'POST':
        cs = mysql.connection.cursor()
        cs.execute('DELETE FROM tb_medicos WHERE id = %s', (id,))
        mysql.connection.commit()
    flash('Mensaje')
    return redirect(url_for('consulta_admin'))

#   MEDICO GENERAL  #

@app.route('/expediente_paciente')
def expediente_paciente():
    cs = mysql.connection.cursor()
    cs.execute('SELECT nombre_completo FROM tb_medicos')
    data = cs.fetchall()
    return render_template('Medico/expediente_paciente.html', medico = data)

@app.route("/expediente_pacienteBD", methods=['POST'])
def registrarPaciente():
    if request.method == 'POST':
        VMEDICO = request.form.get("medico", False)
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

    flash('Mensaje')
    return redirect(url_for('expediente_paciente'))

@app.route('/exploracion')
def exploracion():
    cs = mysql.connection.cursor()
    cs.execute('SELECT nombre_completo FROM tb_pacientes')
    data = cs.fetchall()
    cs.execute('SELECT nombre_completo FROM tb_medicos')
    data2 = cs.fetchall()

    return render_template('Medico/exploraciondiagnostico.html', pacientes = data, medicos = data2)

@app.route('/exploracionBD', methods=['POST'])
def exploracionBD():
    if request.method == 'POST':
        VPACIENTE = request.form.get("paciente", False)
        VMEDICO = request.form.get("medico", False)
        VFECHA = request.form['fechaexp']
        VALTURA = request.form['altura']
        VTEMPERATURA = request.form['temperatura']
        VLATIDOS = request.form['latidos']
        VSATURACION = request.form['saturacion']
        VSINTOMAS = request.form['sintomas']
        VTRATAMIENTO = request.form['tratamiento']
        VESTUDIOS = request.form['estudios']

        cs = mysql.connection.cursor()
        cs.execute('INSERT INTO tb_exploraciones (paciente, medico, fecha, altura, temperatura, latidos, saturacion, sintomas, tratamiento, estudios) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(VPACIENTE, VMEDICO, VFECHA, VALTURA, VTEMPERATURA, VLATIDOS, VSATURACION, VSINTOMAS, VTRATAMIENTO, VESTUDIOS))
        mysql.connection.commit()

    flash('Mensaje')
    return redirect(url_for('exploracion'))

@app.route('/selecpaciente')
def selecpaciente():
    cs = mysql.connection.cursor()
    cs.execute('SELECT paciente FROM tb_exploraciones')
    data = cs.fetchall()
    return render_template('Medico/seleccionpaciente.html', pacientes = data)

@app.route('/consultacitas', methods=['POST'])
def consultacitas():
    if request.method == 'POST':
        VPACIENTE = request.form.get("paciente", False)
        cs = mysql.connection.cursor()
        cs.execute('SELECT id, paciente, fecha, estudios FROM tb_exploraciones where paciente = %s', (VPACIENTE,))
        data = cs.fetchall()
        return render_template('Medico/consultacitas.html', citas = data)


@app.route('/selectmedico')
def consulta_paciente():
    cur = mysql.connection.cursor()
    cur.execute('SELECT nombre_completo FROM tb_medicos')
    data = cur.fetchall()
    return render_template('Medico/seleccionmedico.html', medicos = data)

@app.route('/consultapaciente', methods=['POST'])
def consulta_paciente2():
    if request.method == 'POST':
        VMEDICOC = request.form.get("medico", False)
        cur = mysql.connection.cursor()
        cur.execute('SELECT id, nombre_completo, fecha_nacimiento, enfermedades_cronicas, alergias, antecendentes_familiares FROM tb_pacientes where medico = %s', (VMEDICOC,))
        data = cur.fetchall()
        return render_template('Medico/consultapaciente.html', pacientes = data)
    
@app.route('/actualizacion_paciente/<id>')
def actuadmin2(id):
    cs = mysql.connection.cursor()
    cs.execute('SELECT id, nombre_completo, fecha_nacimiento, enfermedades_cronicas, alergias, antecendentes_familiares FROM tb_pacientes where id = %s', (id,))
    data = cs.fetchall()
    return render_template('Medico/actualizacion_paciente.html', Edicion = data)

@app.route('/actualizacion_pacienteBD/<id>', methods=['POST'])
def actuadminBD2(id):
    if request.method == 'POST':
        VNOMBRE = request.form['Nombre']
        VFECHANAC = request.form['fechanac']
        VENFERMEDAD = request.form['enfermedades']
        VALERGIAS = request.form['alergia']
        VANTECEDENTES = request.form['antecedentes']

        cs = mysql.connection.cursor()
        cs.execute('UPDATE tb_pacientes SET nombre_completo = %s, fecha_nacimiento = %s, enfermedades_cronicas = %s, alergias = %s, antecendentes_familiares = %s WHERE id = %s', (VNOMBRE, VFECHANAC, VENFERMEDAD, VALERGIAS, VANTECEDENTES, id))
        mysql.connection.commit()
    
    flash('Mensaje')
    return redirect(url_for('consulta_paciente'))

@app.route('/generareceta/<id>')
def generareceta(id):
    cs = mysql.connection.cursor()
    cs.execute('SELECT * FROM tb_exploraciones where id = %s', (id,))
    data = cs.fetchall()
    

    return render_template('Medico/receta.html', pacientes = data)


#Ejecucion del servidor

if __name__ == '__main__':
    app.run(port=5000, debug=True)
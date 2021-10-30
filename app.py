from flask import Flask, render_template, request
import db, werkzeug.security as ws

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/iniciar_sesion', methods=['POST'])
def validar_iniciar_sesion():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    registro_usuario = db.obtener_registros('usuario', "usuario = '{}'".format(usuario))

    if registro_usuario:
        contrasena_db = registro_usuario [0][4]

        inicio_exitoso = ws.check_password_hash(contrasena_db, contrasena)

        if inicio_exitoso:
            return 'Inicio sesion exitoso'
        else: 
            return 'Verifique usuario y contrasena'
    else:
        return 'El usuario no existe'

@app.route('/iniciar')
def validar_iniciar():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/registar_usuario', methods=['POST'])
def registar_usuario():
    #validar datos
    nombre = request.form['nombre']
    usuario = request.form['usuario']
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    confirmar_contrasena = request.form['confirmar_contrasena']

    db.insert_usuario(nombre, usuario, correo, ws.generate_password_hash(contrasena))

    return render_template('perfil.html')

@app.route('/retroalimentacion')
def retroalimentacion():
    return render_template('retroalimentacion.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/infodocente')
def infodocente():
    return render_template('info_docente.html')

@app.route('/creactividad')
def creactividad():
    return render_template('creacion_actividad.html')

@app.route('/detactividad')
def detactividad():
    return render_template('detalle_actividad.html')

@app.route('/resultadoBusquedas')
def resultadoBusquedas():
    return render_template('resultadoBusquedas.html')

@app.route('/visualizacionNotas')
def visualizacionNotas():
    return render_template('visualizacionNotas.html')

@app.route('/infoestudiante')
def infoestudiante():
    return render_template('info_estudiante.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')
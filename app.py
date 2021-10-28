from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/iniciar')
def iniciar():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')


@app.route('/retroalimentacion')
def retroalimentacion():
    return render_template('retroalimentacion.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/infodocente')
def infodocente():
    return render_template('info_docente.html')

@app.route('/infoestudiante')
def infoestudiante():
    return render_template('info_estudiante.html')

@app.route('/creactividad')
def creactividad():
    return render_template('creacion_actividad.html')

@app.route('/detactividad')
def detactividad():
    return render_template('detalle_actividad.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')
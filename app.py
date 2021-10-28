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

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')
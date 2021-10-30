import sqlite3
from sqlite3 import Error

def obtener_conexion():
    try:
        conexion = sqlite3.connect('db/basedatos.db')
        return conexion
    except Error:
        print(Error)
    
def obtener_registros(tabla, condicion=None):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    if condicion:
        strsql = 'SELECT * FROM {} WHERE {}'.format(tabla, condicion)
    else:
        strsql = 'SELECT * FROM {}'.format(tabla)

    cursor.execute(strsql)
    datos = cursor.fetchall()
    conexion.close()

    return datos

def insert_usuario(nombre, usuario, correo, contrasena):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    strsql = "INSERT INTO usuario (nombre, usuario, correo, contrasena) VALUES ('{}','{}','{}','{}')".format(nombre, usuario, correo, contrasena)

    cursor.execute(strsql)
    conexion.commit
    conexion.close()


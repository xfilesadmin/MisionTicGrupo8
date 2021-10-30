boton_ver_contrasena = document.getElementById('ver_contrasena')

boton_ver_contrasena.addEventListener('click', () => {
    input_contrasena = document.querySelector('#contrasena')
    tipo_input_contrasena = input_contrasena.getAttribute('type')

    if(tipo_input_contrasena =='password'){
        input_contrasena.setAttribute('type', 'text')
        boton_ver_contrasena.setAttribute('src', '/static/img/noVer.png')
    } else {
        input_contrasena.setAttribute('type', 'password')
        boton_ver_contrasena.setAttribute('src', '/static/img/ver.png')
    }
})

boton_ver_confirmar_contrasena = document.getElementById('ver_confirmar_contrasena')

boton_ver_confirmar_contrasena.addEventListener('click', () => {
    input_contrasena = document.querySelector('#confirmar_contrasena')
    tipo_input_contrasena = input_contrasena.getAttribute('type')

    if(tipo_input_contrasena =='password'){
        input_contrasena.setAttribute('type', 'text')
        boton_ver_confirmar_contrasena.setAttribute('src', '/static/img/noVer.png')
    } else {
        input_contrasena.setAttribute('type', 'password')
        boton_ver_confirmar_contrasena.setAttribute('src', '/static/img/ver.png')
    }
})

function validar_formulario(){
    input_usuario = document.getElementById('usuario')
    input_correo = document.getElementById('correo')
    input_contrasena = document.getElementById('contrasena')
    input_confirmar_contrasena = document.getElementById('confirmar_contrasena')

    if (!validar_usuario(input_usuario.value)) {
        alert('El usuario no puede tener espacios en blanco')
        return false
    }

    if (!validar_correo(input_correo.value)) {
        alert('El correo no es valido')
        return false
    }

    if (!validar_contrasena(input_contrasena.value)) {
        alert('La contrasena debe tener minimo 8 caracteres, una letra mayuscula, una minuscula y un caracter especial')
        return false
    }

    if (input_contrasena.value != input_confirmar_contrasena.value) {
        alert('Las contrasenas no coinciden')
        return false
    }
    return true
}

function validar_usuario(usuario){
    if (/^/S+$/i.test(usuario)) {
        return true
    } else {
        return false
    }
}

function validar_correo(correo){
    if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/i.test(correo)) {
        return true
    } else {
        return false
    }
}

function validar_contrasena(contrasena){
    if (/"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"/i.test(contrasena)) {
        return true
    } else {
        return false
    }
}

boton_iniciar_sesion = document.querySelector()
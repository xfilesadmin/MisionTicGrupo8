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
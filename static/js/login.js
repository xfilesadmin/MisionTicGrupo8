boton_ver = document.querySelector('.ver')

boton_ver.addEventListener('click', () => {
    input_contrasena = document.querySelector('#contrasena')
    tipo_input_contrasena = input_contrasena.getAttribute('type')

    if(tipo_input_contrasena =='password'){
        input_contrasena.setAttribute('type', 'text')
        boton_ver.setAttribute('src', '/static/img/noVer.png')
    } else {
        input_contrasena.setAttribute('type', 'password')
        boton_ver.setAttribute('src', '/static/img/ver.png')
    }
})

boton_registrar = document.querySelector('section div p span')

boton_registrar.addEventListener('click', click_registar)

function click_registar(){
    location.href = '/registro'
}
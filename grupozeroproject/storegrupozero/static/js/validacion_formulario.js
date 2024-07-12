// validacion_formulario.js

function validarFormulario() {
    var nombre = document.getElementById("nombre").value.trim();
    var correo = document.getElementById("correo").value.trim();
    var mensaje = document.getElementById("mensaje").value.trim();
    var errorNombre = document.getElementById("errorNombre");
    var errorCorreo = document.getElementById("errorCorreo");
    var errorMensaje = document.getElementById("errorMensaje");

    // Validación de nombre
    if (nombre === "") {
        errorNombre.innerHTML = "Por favor, ingresa tu nombre.";
        return false;
    } else {
        errorNombre.innerHTML = "";
    }

    // Validación de correo
    if (correo === "") {
        errorCorreo.innerHTML = "Por favor, ingresa tu correo electrónico.";
        return false;
    } else if (!validarCorreo(correo)) {
        errorCorreo.innerHTML = "Por favor, ingresa un correo electrónico válido.";
        return false;
    } else {
        errorCorreo.innerHTML = "";
    }

    // Validación de mensaje
    if (mensaje === "") {
        errorMensaje.innerHTML = "Por favor, ingresa tu mensaje.";
        return false;
    } else {
        errorMensaje.innerHTML = "";
    }

    // Si todas las validaciones son exitosas, el formulario se envía
    return true;
}

function validarCorreo(correo) {
    // Expresión regular para validar correo electrónico
    var re = /\S+@\S+\.\S+/;
    return re.test(correo);
}

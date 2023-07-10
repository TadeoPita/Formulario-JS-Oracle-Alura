
export function valida(input) {
    const tipoDeInput = input.dataset.tipo
    if (validadores[tipoDeInput]) {
        validadores[tipoDeInput](input)
    }

    // console.log(input.parentElement)
    if (input.validity.valid) {
        input.parentElement.classList.remove("input-container--invalid");
        input.parentElement.querySelector("span").innerHTML = "";
    }
    else {
        input.parentElement.classList.add("input-container--invalid");
        input.parentElement.querySelector("span").innerHTML = mostrarMensajeDeError(tipoDeInput, input)

    }
}

const tipoDeErrores = [
    "valueMissing",
    "typeMismatch",
    "patternMismatch",
    "customError",
]

const mensajesDeError = {
    nombre: {
        valueMissing: "Este campo nombre no puede estar vacio"
    },
    email: {
        valueMissing: "Este campo email no puede estar vacio",
        typeMismatch: "El correo no es valido"
    },
    password: {
        valueMissing: "Este campo no puede estar vacio",
        patternMismatch: "Al menos 6 caracteres, maximo 12, debe contener una letra minuscula una letra mayuscula un numero y no puede contener caracteres especiales",
    },
    nacimiento: {
        valueMissing: "Este campo no puede estar vacio",
        customError: "Debes tener al menos 18 años de edad"
    },
    numero:{
        valueMissing: "Este campo no puede estar vacio",
        patternMismatch: "El formato requerido es 11 12345678",
    },
    direccion:{
        valueMissing: "Este campo no puede estar vacio",
        patternMismatch: "La direccion debe contener entre 10 a 40 caracteres",
    },
    provincia:{
        valueMissing: "Este campo no puede estar vacio",
        patternMismatch: "La provincia debe contener entre 4 a 40 caracteres",
    },
    ciudad:{
        valueMissing: "Este campo no puede estar vacio",
        patternMismatch: "La ciudad debe contener entre 4 a 40 caracteres",
    },


}

const validadores = {
    nacimiento: (input) => validarNacimiento(input)
};

function mostrarMensajeDeError(tipoDeInput, input) {
    let mensaje = ""
    tipoDeErrores.forEach(error =>{
        if(input.validity[error]){
            console.log(error)
            console.log(input.validity[error])
            console.log(mensajesDeError[tipoDeInput],[error]);
            mensaje = mensajesDeError[tipoDeInput][error];
        }
    })
    return mensaje
}

const inputNacimiento = document.querySelector("#birth");
// input nacimiento va a tener una accion cuando se toque otro input osea cuando pierde el foco se van a aacionar 2 cosas el blur y el evento, el evento esta acompañado de un funcion que es vlidar nacimiento y se entra al evento. tarqget porque ahi est la guardada la seccion de la fecha de nacimiento
inputNacimiento.addEventListener("blur", (evento) => {
    validarNacimiento(evento.target);
})

function validarNacimiento(input) {
    const fechaCliente = new Date(input.value);
    let mensaje = ""
    if (!mayorEdad(fechaCliente)) {
        mensaje = "Debes tener al menos 18 años de edad"
    }
    input.setCustomValidity(mensaje)
}

function mayorEdad(fecha) {
    const fechaActual = new Date();
    const diferenciaFechas = new Date(fecha.getUTCFullYear() + 18, fecha.getUTCMonth(), fecha.getUTCDate());
    return diferenciaFechas <= fechaActual;
}
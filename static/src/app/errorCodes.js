/**
 * Created by johnmachahuay on 6/26/15.
 */

angular
    .module('app')
    .constant('CODE_ERRORS', {
        100000: {message: "Datos ingresados incorrectamente."},
        100001: {message: "No esta activo el usuario."},
        100002: {message: "El usuario no esta activo."},
        100003: {message: "Hubo un error en la transacción."},
        100004: {message: "Completar los campos de información de pago."},
        100005: {message: "Falló el envio."}
    });
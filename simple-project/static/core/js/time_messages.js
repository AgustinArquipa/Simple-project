
$(document).ready(function() {
    // Espera 4 segundos y luego oculta el mensaje 
    $('.alert-success').each(function() {
        console.log("pasamos el alert");
        var $alert = $(this);
        var autoDismissTimeout = parseInt($alert.data('auto-dismiss')) || 2500; // 4 segundos por defecto
        setTimeout(function() {
            $alert.fadeOut();
        }, autoDismissTimeout);
    });
    $('.alert-danger').each(function() {
        console.log("pasamos el alert");
        var $alert = $(this);
        var autoDismissTimeout = parseInt($alert.data('auto-dismiss')) || 3500; // 4 segundos por defecto
        setTimeout(function() {
            $alert.fadeOut();
        }, autoDismissTimeout);
    });
});
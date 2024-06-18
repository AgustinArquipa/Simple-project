// Evento para el boton cerrar del modal
$('.modal').on('click', '[data-dismiss="modal"]', function() {
    $(this).closest('.modal').modal('hide');
});

// Funcion que me permite cerrar las notificaciones flash
$('.btn-close').click(function() {
    $(this).closest('.alert').fadeOut();
});

// Evento para volver a la parte de configuraciones extras
document.getElementById("back-button").addEventListener("click", function() {
    var url = this.getAttribute("data-url");
    console.log("URL generada:", url);
    window.location.href = url;
});
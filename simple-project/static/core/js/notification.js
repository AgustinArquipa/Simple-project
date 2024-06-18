document.addEventListener('DOMContentLoaded', (event) => {
    // Seleccionamos todos los botones de cierre
    const closeButtons = document.querySelectorAll('.btn-close');
  
    closeButtons.forEach(button => {
      button.addEventListener('click', function() {
        // Seleccionamos el contenedor de la notificación
        const notificationContainer = this.closest('.notification-container');
        
        // Ocultamos el contenedor de la notificación
        notificationContainer.style.display = 'none';
      });
    });
});
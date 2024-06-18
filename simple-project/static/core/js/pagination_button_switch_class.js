const oldClassName = 'dt-paging-button';
const newClassNames = ['btn', 'btn-sm', 'btn-falcon-default', 'me-1'];

// Función para reemplazar las clases
function replaceClasses() {
    const elements = document.querySelectorAll('.' + oldClassName);
    elements.forEach(element => {
        element.classList.remove(oldClassName);
        newClassNames.forEach(newClass => {
            element.classList.add(newClass);
        });
    });
}

// Crear un MutationObserver para detectar cambios en el DOM
const observer = new MutationObserver((mutationsList, observer) => {
    for (const mutation of mutationsList) {
        if (mutation.type === 'childList') {
            replaceClasses();
        }
    }
});

// Configurar el observer para observar el documento completo
observer.observe(document.body, { childList: true, subtree: true });

// También ejecutamos el reemplazo al cargar completamente el DOM
document.addEventListener('DOMContentLoaded', function() {
    replaceClasses();
});
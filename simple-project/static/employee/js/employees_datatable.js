let employeeID;
let table;

$(document).ready(function() {
    // Inicializamos la tabla de datos
    table = initializeDataTable()

    styleDatatable()
    // Llamamos a la función setColumnsWidth
    setColumnsWidth(table)

    // Función que permite cerrar las notificaciones flash
    $('.btn-close').click(function() {
        $(this).closest('.alert').fadeOut();
    });
})

// Función para inicializar el datatable 
function initializeDataTable() {
    let table = document.getElementById("tableEmployee")
    let url = table.getAttribute("data-url")

    // Inicializamos el datatable
    let datatable = $('#tableEmployee').DataTable({
        responsive: true,
        // Configuración para el procesamiento de datos
        processing: true,
        serverSide: true,
        ajax: {
            url: url,
            dataSrc: 'data'
        },
        // Definimos las columnas de la tabla
        columns: [ 
            { data: 'id' },
            { data: 'full_name' },
            { data: 'dni' },
            { data: 'grouping' },
            { data: 'address' },
            { data: 'service' },
            { data: 'status' }
        ],
        // Configuración del idioma y mensajes
        language: {
            lengthMenu: 'Mostrar _MENU_ Productos',
            decimal: "",
            emptyTable: "No hay Propiedad de Servicios que mostrar en la tabla",
            info: "Mostrando _START_ a _END_ de _TOTAL_ registros",
            infoEmpty: "Mostrando 0 de 0 de 0 registros",
            loadingRecords: "Cargando...",
            search: "Buscar:",
            paginate: {
                first: "Primero",
                last: "Último",
                next: "Siguiente",
                previous: "Anterior"
            }
        },
        autoWidth: false,
        columnDefs:[
            {
                targets: 6,
                orderable: false
            }
        ] 
    });

    return datatable;
}


function setColumnsWidth(datatable) {
    // Obtener el número de columnas
    var numColumns = datatable.columns().count();
    // Calcular el ancho de cada columna
    var columnWidth = (100 / numColumns) + '%';
    // Establecer el ancho para todas las columnas
    datatable.columns().every(function () {
        this.width(columnWidth);
    });
}


// funcion para agregar estilos extras al Datatable
function styleDatatable(){
    // Para el scrollbar
    $('.dt-scroll-body').addClass('scrollbar');
    $('.dt-layout-row.dt-layout-table > .dt-layout-cell').addClass(' scrollbar');
    // Para que el boton de nuevo empleado este en el lado derecho
    $('.dt-layout-row > .dt-layout-cell.dt-full ').removeClass('dt-full').addClass('dt-start')

    //estilos row
    $('#tableEmployee').addClass('stripe hover');

}

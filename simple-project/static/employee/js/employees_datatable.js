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
        layout: {
            top2start: function() {
                let toolbar = document.createElement('div')
                toolbar.innerHTML = `
                <div>
                    <a href="${$('#employee_add').data('url')}" class="btn btn-info btn-sm me-1 my-2" type="button">
                        <span class="fas fa-plus" data-fa-transform="shrink-3 down-2"></span>
                        <span class="d-none d-sm-inline-block ms-1">Nuevo Empleado</span>
                    </a>
                    <a href="${$('#lockers').data('url')}" class="btn btn-info btn-sm me-1 my-2" type="button">
                        <span class="fa-solid fa-list" data-fa-transform="shrink-3 down-2"></span>
                        <span class="d-none d-sm-inline-block ms-1">Lista de Casilleros</span>
                    </a>
                    <a href="${$('#patrimonies').data('url')}" class="btn btn-info btn-sm me-1 my-2" type="button">
                        <span class="fa-solid fa-list" data-fa-transform="shrink-3 down-2"></span>
                        <span class="d-none d-sm-inline-block ms-1">Lista de Patrimonios</span>
                    </a>
                </div>`;
                return toolbar
            },
            topStart: {
                pageLength: {
                    menu: [5, 10, 15, 20]
                }
            },
            topEnd: {
                search: {
                    placeholder: "Buscar ..."
                }
            },
            bottomEnd: {
                paging : {
                    numbers: 3
                }
            }
        },
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
            { data: 'service' },
            { data: 'status' },
            { data: 'condition'},
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
        ],
         // Aplicar estilos de fila según la condición
        createdRow: function(row, data, dataIndex) {
            if (data.condition === 'Ocupado') {
                $(row).css('background-color', '#add8e6');
            } else if (data.condition === 'Reservado') {
                $(row).css('background-color', '#fffacd');
            }
        }
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

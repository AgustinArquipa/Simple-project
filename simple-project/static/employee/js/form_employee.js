let url_create;

$(document).ready(function() {
    // Evento para el botón 'confirmar' del formulario
    $("#footer-buttons").on("click", 'button[rel="confirm"]', function () {
        showConfirmModal();
    });


    // Obtener el checkbox de "Crear Usuario"
    const createUserCheckbox = document.getElementById('createUserCheckbox');
    // Obtener la sección del formulario de usuario
    const userFormSection = document.getElementById('userFormSection');
    
    // Verificamos que existan el checkbox para crear en el caso de que seamos superusuarios
    if (createUserCheckbox && userFormSection) {
        // Escuchar cambios en el checkbox
        createUserCheckbox.addEventListener('change', function () {
            // Si el checkbox está marcado, mostrar el formulario de usuario, de lo contrario, ocultarlo
            if (createUserCheckbox.checked) {
                userFormSection.style.display = 'block';
                // Recuperamos los inputs del nombre de usuario, constraseña y repetir contraseña
                $('#id_username').on('input', function () {
                    validateLength(this, 3)
                });
                $('#id_password1').on('input', function() {
                    validateLength(this, 4)
                });
                $('#id_password2').on('input', function() {
                    validateLength(this, 4)
                });

            } else {
                userFormSection.style.display = 'none';
            };
        });
    };
    
    // Modal para location
    url_create = $("#location_add").data("url");
    console.log(url_create);
    
    // Incializamos el Select2
    $('.js-province-basic-single').select2({
        width: '100%',
        dropdownParent: $('#locationAddModal')
    });
    // Inicializamos el Select2 para el pais
    $('.js-country-basic-single').select2({
        width: '100%',
        dropdownParent: $('#locationAddModal')
    });

    /******************************************************************************************************************
    *                               Validaciones a Tiempo Real                                                      *
    *****************************************************************************************************************/
    // Añadir asteriscos a los labels de los campos obligatorios
    $('input[required], select[required], textarea[required]').each(function() {
        const label = $(`label[for="${this.id}"]`);
        label.append(' <span style="color: red;">*</span>');
        if(this.value == ''){
            setInvalid(this)
        }
    });

    // Validaciones en tiempo real y restricciones de entrada
    $('input, select, textarea').each(function() {
        // Cada iteración representa un elemento de entrada (input, select o textarea)
        const input = $(this);
        
        if (input.attr('id') === 'id_dni' || input.attr('id') === 'id_cuil') {
            input.on('input', function() {
                // Función de validación o restablecimiento según el tipo de campo
                validateLength(this, 5);
            });
            input.on('keypress', restrictToNumbers);
            // Función para restringir la entrada de caracteres según el tipo de campo
        } else if (input.is('#id_first_phone, #id_second_phone, #id_phone_reference')) {
            input.on('input', function() {
                // Función de validación o restablecimiento según el tipo de campo
                validatePhone(this);
            });
            input.on('keypress', restrictToNumbers);
            // Función para restringir la entrada de caracteres según el tipo de campo

        } else if (input.attr('id') === 'id_salary') {
            input.on('input', function() {
                validateSalary(this);
            });
            input.on('keypress', restrictToNumbers);
            // Función para restringir la entrada de caracteres según el tipo de campo
        } else if (input.is('#id_email')) {
            input.on('input', function(){
                // Funcion que valida el formato del correo electronico
                validateEmail(this);
            });
        }
        else {
            input.on('input', function() {
                resetValidation(this);
            });
        }
    });

    /******************************************************************************************************************
    *                               FIN de Validaciones a Tiempo Real                                               *
    *****************************************************************************************************************/

});

// Evento para el boton cerrar del modal
$('.modal').on('click', '[data-dismiss="modal"]', function() {
    $(this).closest('.modal').modal('hide');
});

// Modal para confirmar la creacio/actualizacion
function showConfirmModal() {
    
    $("#confirmEmployee").modal("show");

    // Adjuntar un evento al botón de confirmación dentro del modal
    $("#confirmCreate").off("click").on("click", function(event) {
        
        event.preventDefault(); // Evitar que se recargue la página
        $('#employee-create').submit();
        // Cierra el modal de confirmación
        $('#confirmEmployee').modal('hide');
    });
}



/*#######################################################################
                   Modal de Location
######################################################################*/




// Evento para cuando hacemos click en el boton podamos abrir el modal de location
$('#addLocation').click(function() {
    //createButton()
    $('#locationAddModal').modal('show')
    clearForm('form_add_location'); // Vaciar el formulario al mostrar el modal

});

// Evento para cuando doy click al boton de confirmar en el formualrio
$('#confirmLocation').click(function(e) {
    e.preventDefault(); // Evita que se recargue la página al hacer clic en el enlace
    // Recuperamos el formulario con los datos
    const csrfToken = $('input[name=csrfmiddlewaretoken]').val()
    let form = document.getElementById("form_add_location")
    let formData = new FormData(form)
    
    // let formData = {
    //     'name': $('#id_name_location').val(),
    //     'province': $('#id_province').val(),
    //     'country': $('#id_country').find('option:selected').text().trim()
    // }
    // console.log("Formulario -> ", formData);

    // Agregamos evento para cuando hacemos click en el boton guardar
    $.ajax({
        type: 'POST',
        url: url_create,
        headers: { 'X-CSRFToken': csrfToken },
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            console.log(response);
            response.data.location = capitalizarPrimeraLetra(response.data.location); 
            
            var option = new Option(response.data.location, response.data.id, true, true);

            $('#id_location').append(option).trigger('change');
            $('#locationAddModal').modal('hide')
        }
    });

});

// Evento para el boton cerrar del modal
$('.modal').on('click', '[data-dismiss="modal"]', function() {
    $(this).closest('.modal').modal('hide');
});

// Funcion que me permite cerrar las notificaciones flash
$('.btn-close').click(function() {
    $(this).closest('.alert').fadeOut();
});

// Función para vaciar los campos del formulario
function clearForm(formId) {
    $('#' + formId)[0].reset(); // Utilizar reset() para vaciar el formulario

    // Si hay campos de selección con Select2, restablecerlos también
    $('#' + formId + ' select').each(function() {
        var selectId = $(this).attr('id');
        if (selectId) {
            $('#' + selectId).val('').trigger('change');
        }
    });
}

// funcion para poner la primera letra en mayuscula
function capitalizarPrimeraLetra(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}


/******************************************************************************************************************
*                        Funciones para las Validaciones a Tiempo Real                                       *
*****************************************************************************************************************/

function validateLength(input, minLength) {
    if (input.value === "") {
        resetValidation(input);
    } else if (input.value.length > minLength) {
        setValid(input);
    } else {
        setInvalid(input, `Debe tener más de ${minLength} caracteres.`);
    }
}

function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email.value === ""){
        resetValidation(email);
    }
    else if (regex.test(email.value)){
        setValid(email);
    } else {
        setInvalid(email);
    } 
}

function validatePhone(input) {
    const value = input.value;
    const regex = /^\+?[0-9]+$/;
    if (value === "") {
        resetValidation(input);
    } else if (value.length >= 6 && value.length <= 15 && regex.test(value)) {
        setValid(input);
    } else {
        setInvalid(input, 'El teléfono debe tener entre 6 y 15 caracteres y solo puede contener números y el símbolo "+".');
    }
}

function validateSalary(input) {
    const value = parseFloat(input.value);
    if (input.value === "") {
        resetValidation(input);
    } else if (!isNaN(value) && value > 0) {
        setValid(input);
    } else {
        setInvalid(input, 'El salario debe ser un número positivo.');
    }
}

// Funcion que nos restinge ingresar letras en los campos numericos
function restrictToNumbers(event) {
    if ((event.key < '0' || event.key > '9')&&(event.key !== '+' && event.key !== '-')) {
        event.preventDefault();
    }
}

// Las funciones SET coloca las clases de color verde para validado y color rojo para invalidado
function setValid(input) {
    input.classList.remove('is-invalid');
    input.classList.add('is-valid');
    input.setCustomValidity('');
}

function setInvalid(input, message) {
    input.classList.remove('is-valid');
    input.classList.add('is-invalid');
    input.setCustomValidity(message);
}

// Funcion que nos permite sacar los bordes de las validaciones
function resetValidation(input) {
    input.classList.remove('is-valid');
    input.classList.remove('is-invalid');
    input.setCustomValidity('');
}
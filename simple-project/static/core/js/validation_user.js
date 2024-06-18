$(document).ready(function() {
		$.ajax({
				url: "/api/user_permissions/",
				type: "GET",
				success: function(data) {
						var super_user = data.is_superuser;
						var staff_user = data.is_staff;

						console.log("Super User: ", super_user);
						console.log("Staff User: ", staff_user);
						
						// Utiliza estas variables según sea necesario
						if (!(super_user || staff_user)) {
								// Mostrar botón de "Nueva Propiedad"
								$('#property_create_button').hide();
						}
				},
				error: function(error) {
						console.log("Error fetching user permissions: ", error);
				}
		});
});

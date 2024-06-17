from django.utils import path
from views import create_employee

app_name = 'employee_app'

urlpatterns = [
    path(
        "",
        create_employee,
        name="create_employee"
    ),
]

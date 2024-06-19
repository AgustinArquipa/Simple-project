from django.urls import path
from .views import *

app_name = 'employee_app'

urlpatterns = [
    path(
        "create/",
        create_employee,
        name="create_employee"
    ),
    path(
        "list/",
        employee_list,
        name="list"
    ),
    path(
        "list-datatable/",
        EmployeeAjaxView,
        name="employee_datatable"
    ),
    path(
        "list-context/",
        employee_list_view,
        name="employee_list_code"
    )
]

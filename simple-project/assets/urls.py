from django.urls import path
from .views import *

app_name = 'assets_app'

urlpatterns = [
    path(
        'list/',
        patrimony_list,
        name="list_patrimony"
    ),
    path(
        'list-datatable',
        PatrimonyAjaxView,
        name="list_datatable"
    ),
    path(
        'create/',
        create_patrimony,
        name="create_patrimony"
    )
]

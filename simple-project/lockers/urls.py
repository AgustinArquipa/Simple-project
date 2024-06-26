from django.urls import path
from .views import *

# create code here

app_name = 'locker_app'

urlpatterns = [
    path(
        'list/',
        locker_list,
        name="list_locker"
    ),
    path(
        'list-ajax/',
        LockerAjaxView,
        name="locker_datatable"
    ),
    path(
        'create/',
        create_locker,
        name="locker_create"
    ),
]

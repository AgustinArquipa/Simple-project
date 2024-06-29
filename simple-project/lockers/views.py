from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Locker
from .forms import LockerForm
from core.utils import getColumnsForModel
from django.http import JsonResponse
from django.db.models import Q, F

# Create your views here.
def create_locker(request):
    from employee.models import Employee
    from assets.models import Patrimony

    if request.method == "POST":
        form = LockerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('locker_app:list_locker')
    else:
        form = LockerForm()

    context = {
        'form': form,
        'employee_count': Employee.objects.get_employee_already(),
        'patrimony_count': Patrimony.objects.get_patrimony_already()
    }

    return render(request, 'locker/locker_form.html', context)

# Creacion de la lista para las taquillas usando datatable
def locker_list(request):

    urls = [
        {'id': 'locker_add', 'name': 'locker_app:locker_create'},
        {'id': 'employee_list', 'name': 'employee_app:list'}
    ]
    
    context = {
        'columns': getColumnsForModel(Locker, exclude_fields='id'),
        'url_datatable': reverse('locker_app:locker_datatable'),
        'urls': urls
    }

    return render(request, 'locker/locker_list.html', context)

def LockerAjaxView(request):
    draw = request.GET.get('draw')
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    order_column_index = int(request.GET.get('order[0][column]', 0))
    order_direction = request.GET.get('order[0][dir]', 'asc')
    search_value = request.GET.get('search[value]', None)

    # Mapeo de indices de columnas 
    column_mapping = {
        0: 'number_locker',
        1: 'status_locker',
        2: 'employee',
        3: 'patrimony'
    }

    order_column = column_mapping.get(order_column_index, 'number_locker')
    if order_direction == 'asc':
        order_column = F(order_column).asc(nulls_last=True)
    else:
        order_column = F(order_column).desc(nulls_last=True)

    # Armamos de manera dinamica las condiciones de busqueda 
    conditions = Q()
    if search_value:
        fields = [
            'number_locker', 'status_locker', 'employee__full_name', 'patrimony__number_patrimony'
        ]

        search_terms = search_value.split()

        for term in search_terms:
            # Para cada palabra buscamos campos relevantes
            term_conditions = Q()
            for field in fields:
                term_conditions |= Q(**{f"{field}__icontains": term})
            
            conditions &= term_conditions

    filtered_data = Locker.objects.filter(conditions)
    filtered_data = filtered_data.order_by(order_column)

    total_records = filtered_data.count()

    data = [
        item.to_json()
        for item in filtered_data[start: start+length]
    ]
    

    return JsonResponse(
        {
            'draw': draw,
            'recordsTotal': total_records,
            'recordsFiltered': total_records,
            'data': data
        }
    )
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EmployeeForm
from .models import Employee
from core.utils import getColumnsForModel
from django.http import JsonResponse
from django.db.models import Q, F

# Create your views here.
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_app:list')  # Redirige a la lista de empleados o a donde prefieras
    else:
        form = EmployeeForm()
    
    return render(request, 'employee/employee_form.html', {'form': form})

def employee_list(request):

    urls = [
        {'id':'employee_add', 'name':'employee_app:create_employee'},
        {'id': 'lockers', 'name':'locker_app:list_locker'}
    ]

    context = {
        'columns': getColumnsForModel(Employee),
        'url_datatable': reverse("employee_app:employee_datatable"),
        'urls': urls
    }

    return render(request, 'employee/employee_list.html', context)

def employee_list_view(request):
    # Devolvemos los datos atraves de un contexto
    columns = getColumnsForModel(Employee)
    data = Employee.objects.all()
    context = {
        'columns': columns,
        'employee': data,
        'url_datatable': reverse("employee_app:employee_datatable"),
        'datos_context': 1
    }
    return render(request, 'employee/employee_list.html', context)

def EmployeeAjaxView(request):
    draw = request.GET.get('draw')
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    order_column_index = int(request.GET.get('order[0][column]', 0))
    order_direction = request.GET.get('order[0][dir]', 'asc')
    search_value = request.GET.get('search[value]', None)

    # Mapeo de indices de columnas 
    column_mapping = {
        0: 'id',
        1: 'full_name',
        2: 'dni',
        3: 'gruoping',
        4: 'service',
        5: 'status',
        6: 'condition'
    }

    order_column = column_mapping.get(order_column_index, 'id')
    if order_direction == 'asc':
        order_column = F(order_column).asc(nulls_last=True)
    else:
        order_column = F(order_column).desc(nulls_last=True)

    # Armamos de manera dinamica las condiciones de busqueda 
    conditions = Q()
    if search_value:
        fields = [
            'dni', 'full_name', 'status', 'gruoping', 'id', 'condition', 'service'
        ]

        search_terms = search_value.split()

        for term in search_terms:
            # Para cada palabra buscamos campos relevantes
            term_conditions = Q()
            for field in fields:
                term_conditions |= Q(**{f"{field}__icontains": term})
            
            conditions &= term_conditions

    filtered_data = Employee.objects.filter(conditions)
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
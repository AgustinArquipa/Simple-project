from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PatrimonyForm
from .models import Patrimony
from core.utils import getColumnsForModel
from django.http import JsonResponse
from django.db.models import Q, F

# Create your views here.
def create_patrimony(request):
    if request.method == 'POST':
        form = PatrimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assets_app:list_patrimony')  # Redirige a la lista de empleados o a donde prefieras
    else:
        form = PatrimonyForm()
    
    return render(request, 'assets/patrimony_form.html', {'form': form})

def patrimony_list(request):

    urls = [
        {'id': 'patrimony_add', 'name':'assets_app:create_patrimony'},
        {'id':'employees', 'name':'employee_app:list'},
        {'id': 'lockers', 'name':'locker_app:list_locker'}
    ]

    list_columns = getColumnsForModel(Patrimony)
    list_columns.append('Taquillas')

    context = {
        'columns': list_columns,
        'url_datatable': reverse("assets_app:list_datatable"),
        'urls': urls
    }

    return render(request, 'assets/patrimionies_list.html', context)


def PatrimonyAjaxView(request):
    draw = request.GET.get('draw')
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    order_column_index = int(request.GET.get('order[0][column]', 0))
    order_direction = request.GET.get('order[0][dir]', 'asc')
    search_value = request.GET.get('search[value]', None)

    # Mapeo de indices de columnas 
    column_mapping = {
        0: 'id',
        1: 'number_patrimony',
        2: 'location'
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
            'id', 'number_patrimony', 'location'
        ]

        search_terms = search_value.split()

        for term in search_terms:
            # Para cada palabra buscamos campos relevantes
            term_conditions = Q()
            for field in fields:
                term_conditions |= Q(**{f"{field}__icontains": term})
            
            conditions &= term_conditions

    filtered_data = Patrimony.objects.filter(conditions)
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
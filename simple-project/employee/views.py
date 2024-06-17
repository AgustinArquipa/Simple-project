from django.shortcuts import render, redirect
from .forms import EmployeeForm

# Create your views here.
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirige a la lista de empleados o a donde prefieras
    else:
        form = EmployeeForm()
    
    return render(request, 'employee_form.html', {'form': form})

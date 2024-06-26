from django import forms
from .models import Employee, STATUS_TYPES

class EmployeeForm(forms.ModelForm):
    full_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre completo del empleado.'
            }
        )
    )
    dni = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el DNI del empleado.'
            }
        )
    )
    gruoping = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el grupo perteneciente del empleado.'
            }
        )
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la direccion del empleado.'
            }
        )
    )
    service = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el servicio.'
            }
        )
    )
    status = forms.CharField(
        widget=forms.Select(
            attrs={
                'class': 'form-control js-status-basic-single'
            },
            choices=[('', 'Seleccione un estado.')] + STATUS_TYPES 
        )
    )
    class Meta:
        model = Employee
        fields = [
            'full_name', 'dni', 'gruoping', 'address', 'service', 'status'
        ]
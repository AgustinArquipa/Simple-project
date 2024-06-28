from django import forms
from .models import Locker, STATUS_LOCKER
from employee.models import Employee
from assets.models import Patrimony

class LockerForm(forms.ModelForm):
    number_locker = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el numero del casillero.'
            }
        )
    )
    status_locker = forms.CharField(
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            },
            choices=[('', 'Seleccione un Estado del casillero.')] + STATUS_LOCKER
        )
    )
    employee = forms.ModelChoiceField(
        required=False,
        queryset=Employee.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
    patrimony = forms.ModelChoiceField(
        required=True,
        queryset=Patrimony.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Locker
        fields = '__all__'
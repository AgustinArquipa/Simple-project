from django import forms
from .models import Patrimony

class PatrimonyForm(forms.ModelForm):
    number_patrimony = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el N° Patrimonial. Ej: 04020101003000326'
            }
        )
    )
    location = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ubicacion del Patriminio. Ej: Laboratorio'
            }
        )
    )

    class Meta:
        model = Patrimony
        fields = '__all__'
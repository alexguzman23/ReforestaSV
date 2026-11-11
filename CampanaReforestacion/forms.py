from django import forms
from .models import CampanaReforestacion

class CampanaReforestacionForm(forms.ModelForm):
    class Meta:
        model = CampanaReforestacion
        fields = ['nombre', 'fecha_inicio', 'institucion_beneficiaria', 'cantidad_proyectada']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'institucion_beneficiaria': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_proyectada': forms.NumberInput(attrs={'class': 'form-control'}),
        }
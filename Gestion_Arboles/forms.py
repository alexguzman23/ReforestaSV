from django import forms
from .models import Arbol

class ArbolForm(forms.ModelForm):
    class Meta:
        model = Arbol
        fields = ['codigo_unico', 'fecha_plantacion', 'estado_salud', 'campana', 'especie', 'ubicacion', 'responsable']
        widgets = {
            'codigo_unico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. ARB-2024-001'}),
            'fecha_plantacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado_salud': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Activo/Sano'}),
            'campana': forms.Select(attrs={'class': 'form-select'}),
            'especie': forms.Select(attrs={'class': 'form-select'}),
            'ubicacion': forms.Select(attrs={'class': 'form-select'}),
            'responsable': forms.Select(attrs={'class': 'form-select'}),
        }
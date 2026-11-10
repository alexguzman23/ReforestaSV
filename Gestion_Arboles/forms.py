from django import forms
from .models import Arbol, Especie

class ArbolForm(forms.ModelForm):
    class Meta:
        model = Arbol
        fields = ['codigo_unico', 'fecha_plantacion', 'estado_salud', 'campana', 'especie', 'ubicacion', 'responsable']
        widgets = {
            'codigo_unico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. ARB-2024-001'}),
            'fecha_plantacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado_salud': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Excelente/Bueno'}),
            'campana': forms.Select(attrs={'class': 'form-select'}),
            'especie': forms.Select(attrs={'class': 'form-select'}),
            'ubicacion': forms.Select(attrs={'class': 'form-select'}),
            'responsable': forms.Select(attrs={'class': 'form-select'}),
        }


class EspecieForm(forms.ModelForm):
    class Meta:
        model = Especie
        fields = ['nombre_comun', 'nombre_cientifico', 'familia', 'tipo_suelo', 'estado_conservacion']
        widgets = {
            'nombre_comun': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Maquilishuat'}),
            'nombre_cientifico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Tabebuia rosea'}),
            'familia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Bignoniaceae'}),
            'tipo_suelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Franco-arcilloso'}),
            'estado_conservacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Estable'}),
        }
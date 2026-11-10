from django import forms
from .models import Arbol, Especie, Ubicacion, Mantenimiento 

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
        
# ==========================================
# FORMULARIO UBICACIONES
# ==========================================

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['zona_referencia', 'latitud', 'longitud']

        widgets = {
            'zona_referencia': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Parque central'
            }),
            'latitud': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. 13.6929400',
                'step': '0.0000001'
            }),
            'longitud': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. -89.2181900',
                'step': '0.0000001'
            }),
        }

# ==========================================
# FORMULARIO DE MANTENIMIENTO
# ==========================================

class MantenimientoForm(forms.ModelForm):

    fecha_actividad = forms.DateTimeField(
        input_formats=[
            "%Y-%m-%dT%H:%M",
            "%Y-%m-%dT%H:%M:%S",
        ],
        widget=forms.DateTimeInput(
            format="%Y-%m-%dT%H:%M",
            attrs={
                "type": "datetime-local",
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Mantenimiento

        fields = [
            "arbol",
            "tipo_actividad",
            "fecha_actividad",
            "comentarios",
        ]

        widgets = {
            "arbol": forms.Select(
                attrs={"class": "form-select"}
            ),

            "tipo_actividad": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. Poda, riego o fertilización",
                }
            ),

            "comentarios": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "maxlength": 255,
                    "placeholder": "Describe el mantenimiento realizado",
                }
            ),
        }

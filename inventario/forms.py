from django import forms
from .models import Notebook

class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = ['codigo', 'marca', 'modelo', 'estado', 'disponible']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
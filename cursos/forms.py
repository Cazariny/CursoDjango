from django import forms
from .models import Curso
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre','descripcion', 'precio', 'cupo', 'imagen']
        widgets = {
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
}
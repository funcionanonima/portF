from django import forms

from .models import Studies, Experience

class AddStudyForm(forms.ModelForm):
    """formulario para mostrar estudios"""
    show = forms.Textarea()
    class Meta:
        model = Studies
        fields = (
            'name',
            'gradedate',
            'school',
            'show',
        )

class AddExperience(forms.ModelForm):
    """formulario para agregar una nueva "esperiencia"""
    class Meta:
        model = Experience
        fields = (
            'appointment',
            'startdate',
            'enddate',
            'company',
            'show',
        )
            
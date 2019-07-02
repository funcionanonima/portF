from django import forms

from .models import Studies, Experience

class AddStudyForm(forms.ModelForm):
    """formulario para mostrar estudios"""
    show = forms.BooleanField(widget=forms.CheckboxInput(attrs={'type':'checkbox','class':'filled-in','checked':'checked'}))
    class Meta:
        model = Studies
        fields = (
            'name',
            'gradedate',
            'school',
            'show',
        )

class AddExperienceForm(forms.ModelForm):
    """formulario para agregar una nueva "experiencia"""
    class Meta:
        model = Experience
        fields = (
            'appointment',
            'startdate',
            'enddate',
            'company',
            'show',
        )
            
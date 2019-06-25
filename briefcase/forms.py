from django import forms

from .models import Studies

class AddStudyForm(forms.ModelForm):
    show = forms.Textarea()
    class Meta:
        model = Studies
        fields = (
            'name',
            'gradedate',
            'school',
            'show',
        )
            
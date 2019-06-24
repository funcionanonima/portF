from django import forms

from .models import Message

class ContactForm(forms.ModelForm):
    email = forms.EmailField()
    name = forms.CharField()    
    body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Message
        fields = ('email', 'name', 'body')
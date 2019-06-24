from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#cre formulariode registro personalizado HEREDANDO DE USERCREATIONFORM
class RegistrationForm(UserCreationForm):
    #los campos de más que quiero agregar:
    email = forms.EmailField(required=True)

    # Defino parametros meta
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password1',
            'password2'
        ]
    
    #metodo save(), para gaurdar SELF o mejor dicho para gaurdar LOSDATOSDELFORMULARIO en el modelo
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)

        if commit:
            user.save()
        
        return user

class EditProfileform(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password'
        ]
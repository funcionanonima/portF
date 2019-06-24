from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
#modulo para evitar que se cere sesion al cambiar contraseña
from django.contrib.auth import update_session_auth_hash
#decorador para validar sesion
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, EditProfileform, InfoForm

# Create your views here.

def Register(request):
    if request.method == 'POST': 
        form = RegistrationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
        return redirect('/account') 
    else: 
        form = RegistrationForm() 
    return render(request,'accounts/register.html',{'form':form})

@login_required
def Profile(request):
    args = {'user':request.user}
    return render(request, 'accounts/profile.html', args)

@login_required
def Info(request):
    if request.method == 'POST':
        form = InfoForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = InfoForm(instance=request.user.userprofile)
        args = {'form':form}
    return render(request, 'accounts/info.html', args)

@login_required
def Edit(request):
    if request.method == 'POST':
        form = EditProfileform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = EditProfileform(instance=request.user)
        args = {'form':form}
    return render(request, 'accounts/edit.html', args)

@login_required
def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile')
        else:
            return redirect('accounts:changepassword')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
    return render(request, 'accounts/changepassword.html', args)
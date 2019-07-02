from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Studies, Experience
from accounts.models import UserProfile
from django.contrib.auth.models import User

from .forms import AddStudyForm, AddExperienceForm

# Create your views here.
class StudyMain(TemplateView):
    template_name = 'studies/studies.html'

# metodo get para traer el formulario
    def get(self, request, id=None):
        if id:
            studies = Studies.objects.get(id=id)
            form = AddStudyForm(instance=studies)
        else:
            form = AddStudyForm()
        studies = Studies.objects.filter(user=request.user)
        args = {
            'form':form,
            'studies':studies,
            }
        return render(request, self.template_name, args)
    
# metodo post para guardar en el modelo
    def post(self, request, id=None):
        if id:
            form = AddStudyForm(request.POST)
            if form.is_valid():
                studyE = form.save(commit=False)
                studyE.id=id
                studyE.user=request.user
                studyE.save()
            return redirect('briefcase:studies')
        form = AddStudyForm(request.POST)
        if form.is_valid():
        # evito que haga el commit de save()
            study = form.save(commit=False)
        # agrego el campo de usuario almacenado en el request
            study.user = request.user
        # save :)
            study.save()
        # vacio el formulario
            form = AddStudyForm()
        # redirecciono
            return redirect('briefcase:studies')
        
        args = {'form':form}
        return render(request, self.template_name, args)

class ExperienceMain(TemplateView):
    template_name = 'experience/experience.html'
    
    def get(self, request, id=None):
        if id:
            exp = Experience.objects.get(id=id)
            form = AddExperienceForm(instance=exp)
        else:
            form = AddExperienceForm()
        exp = Experience.objects.filter(user=request.user)
        args = {
            'form':form, 'exp':exp
            }
        return render(request, self.template_name, args)

    def post(self, request, id=None):
        if id:
            form = AddExperienceForm(request.POST)
            if form.is_valid():
                expe = form.save(commit=False)
                expe.id=id
                expe.user=request.user
                expe.save()
            return redirect('briefcase:experiences')
        form = AddExperienceForm(request.POST)
        if form.is_valid():
            # detener que guarde el objeto para agregarle un campo automatico
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            form = AddExperienceForm()
            return redirect('briefcase:experiences')
        args = {'form':form}
        return render(request, self.template_name, args)

def curriculum(request, id=None):
    if id:
        user = User.objects.get(id=id)
        params = UserProfile.objects.get(user=id)
        studies = Studies.objects.filter(user=id)
        experience = Experience.objects.filter(user=id)
        args = {
            'user':user,
            'params':params,
            'studies':studies,
            'experience':experience,
        }
        return render(request, 'curriculum/param.html', args)
    params = UserProfile.objects.get(user=request.user)
    studies = Studies.objects.filter(user=request.user)
    experience = Experience.objects.filter(user=request.user)
    args = {
        'params':params,
        'studies':studies,
        'experience':experience,
    }
    return render(request, 'curriculum/index.html', args)

def studydelete(request, id=None):
    Studies.objects.get(id=id).delete()
    return redirect('briefcase:studies')

def experiencedelete(reqest, id=None):
    Experience.objects.get(id=id).delete()
    return redirect('briefcase:experiences')
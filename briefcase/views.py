from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Studies, Experience

from .forms import AddStudyForm, AddExperience

# Create your views here.
class StudyMain(TemplateView):
    template_name='studies/studies.html'

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
    def post(self, request):
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
            form = AddExperience(instance=exp)
        else:
            form = AddExperience()
        exp = Experience.objects.all()
        args = {'form':form, 'exp':exp}
        return render(request, self.template_name, args)
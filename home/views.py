"""metodos para pagina ppal"""
from django.views.generic import TemplateView

from django.shortcuts import render, redirect

from .forms import ContactForm

from accounts.models import User

class HomeView(TemplateView):
    """renderiza pagina ppal"""
    template_view = 'home/home.html'

    def get(self, request):
        """pintar el formulariio por metodo get"""
        form = ContactForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        """enviar datos de formulario de contacto"""
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()            
            text = form.cleaned_data
            form = ContactForm()
            return redirect('home:home')
        args = {'form':form, 'text':text}
        return render(request, self.template_name, args)

def curriculums(request):
    users = User.objects.all()
    args = {
        'users':users
    }
    return render(request, 'curriculums/index.html', args)
        
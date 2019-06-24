from django.views.generic import TemplateView

from django.shortcuts import render, redirect

from .forms import ContactForm

class HomeView(TemplateView):
    template_view = 'home/home.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            #para relciones
            # mess = form.save(commit=False)
            # mess.user = request.user
            # mess.save
            
            text = form.cleaned_data
            form = ContactForm()
            return redirect('home:home')

        args = {'form':form, 'text':text}
        return render(request, self.template_name, args)
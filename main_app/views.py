from django.shortcuts import render, redirect

# views imports
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView


# local imports
from main_app.models import Client, Motorcycle
from .forms import SignUpFormClient, SignUpFormTech 

#auth imports
from django.contrib.auth import login

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SignUpFormTech()
        return context 

    def post(self, request):
        form = SignUpFormTech(request.POST)
        if form.is_valid():
            client = form.save()
            login(request, client)
            return redirect('about')
        else: 
            context = {'form': form}
            return render(request, 'home.html', context)
    
class About(TemplateView):
    template_name = 'about.html'

class MotoShow(TemplateView): 
    model = Motorcycle
    template_name = 'client/moto_show.html'
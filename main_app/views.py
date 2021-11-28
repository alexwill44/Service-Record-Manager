from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

# views imports
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, CreateView
# local imports
from main_app.models import Motorcycle, Record
from .forms import SignUpFormClient, SignUpFormTech 

#auth imports
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SignUpFormClient()
        return context 

    def post(self, request):
        form = SignUpFormClient(request.POST)
        if form.is_valid():
            client = form.save()
            login(request, client)
            return redirect('moto_show')
        else: 
            context = {'form': form}
            return render(request, 'home.html', context) 
class About(TemplateView):
    template_name = 'about.html'

""" 
Motorcycle  
"""

### This view includes create/list/search 
class MotoCreate(CreateView):
    model = Motorcycle
    fields = ['make', 'model', 'color', 'dom', 'vin', 'mileage', 'img', 'owner']
    template_name = 'moto_show.html'
### Create New Moto
    def get_success_url(self):
        return reverse ('moto_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MotoCreate, self).form_valid(form)
### Searchbar 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['motorcycles'] = Motorcycle.objects.all()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vin = self.request.GET.get('vin')
        context["header"] = 'Search By Vehical Identification Number'
        
        if vin != None: 
            context['results'] = Motorcycle.objects.filter(vin__icontains=vin)
            count = len(context['results'])
            context["header"] = f'Found {count} with a VIN that contains "{vin}"'
            return context
        else: 
            context["header"] = f'{vin} is not in the database please check the entry or add a new motorcycle to the database'
            return context 

class MotoDelete(View):
    def post(self, request, pk): 
        Motorcycle.objects.filter(pk=pk).delete()
        return redirect(request.META.get('HTTP_REFERER', '/')) 


class MotoDetail(DetailView):
    model = Motorcycle
    template_name = 'moto_detail.html'


""" 
Record 
"""

class RecordCreate(View):
    def post(self, request, pk):
        mileage = request.POST.get('mileage')
        description =  request.POST.get('description')
        parts = request.POST.get('parts')
        motorcycle = Motorcycle.objects.get(pk=pk)
        tech = User.objects.get(pk=pk)
        Record.objects.create(mileage=mileage, description=description, parts=parts, motorcycle=motorcycle, tech=tech )
        return redirect('moto_detail', pk=pk)
   



   
    fields = ['mileage', 'description', 'parts']
    



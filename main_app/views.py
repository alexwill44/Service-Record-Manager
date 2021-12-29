from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

# views imports
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

# local imports
from main_app.models import Motorcycle, Record, Tech, Part
from .forms import SignUpFormClient, SignUpFormTech, CreateRecordForm 

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
            return render(request, 'registration/signup.html', context) 
            
class About(TemplateView):
    template_name = 'about.html'

class TechCreate(TemplateView):
    template_name = 'tech_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SignUpFormTech()
        return context 

    def post(self, request):
        form = SignUpFormTech(request.POST)
        if form.is_valid():
            tech = form.save()
            login(request, tech)
            return redirect('/')
        else: 
            context = {'form': form}
            return render(request, 'tech_create.html', context) 
""" 
Motorcycle  
"""
@method_decorator(login_required(login_url='/'), name='dispatch')
### This view includes create/list/search 
class MotoCreate(CreateView):
    model = Motorcycle
    fields = ['make', 'model', 'color', 'dom', 'vin', 'mileage', 'img', 'owner']
    template_name = 'moto_list.html'
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
            context["header"] = f'Found {count} with a VIN that contains {vin}'
            return context
        else: 
            return context 

@method_decorator(login_required(login_url='/'), name='dispatch')
class MotoDelete(View):
    def post(self, request, pk): 
        Motorcycle.objects.filter(pk=pk).delete()
        return redirect(request.META.get('HTTP_REFERER', '/')) 

@method_decorator(login_required(login_url='/'), name='dispatch')
class MotoDetail(DetailView):
    model = Motorcycle
    template_name = 'moto_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parts'] = Part.objects.all()
        context['form'] = CreateRecordForm
        return context
    
@method_decorator(login_required(login_url='/'), name='dispatch')
class MotoStatusUpdate(View):

    def get(self, request, pk, st):
        if st == 0 :
            Motorcycle.objects.filter(pk=pk).update(status=st)
        if st == 1 :
            Motorcycle.objects.filter(pk=pk).update(status=st)
        if st == 2 :
            Motorcycle.objects.filter(pk=pk).update(status=st)
        if st == 3 :
            Motorcycle.objects.filter(pk=pk).update(status=st)
        if st == 4 :
            Motorcycle.objects.filter(pk=pk).update(status=st)
        if st == 5 :
            Motorcycle.objects.filter(pk=pk).update(status=st)
        if st == 6 :
            Motorcycle.objects.filter(pk=pk).update(status=st)
        return redirect(request.META.get('HTTP_REFERER', '/'))        

""" 
Record 
"""
@method_decorator(login_required(login_url='/'), name='dispatch')
class RecordCreate(CreateView):
    
    def post(self, request, pk, user_pk):
        motorcycle = Motorcycle.objects.get(pk=pk)
        tech = Tech.objects.get(pk=user_pk)
        mileage = request.POST.get('mileage')
        description = request.POST.get('description')
        parts = request.POST.getlist('parts')
        instance = Record.objects.create(mileage=mileage, description=description, motorcycle=motorcycle, tech=tech )
        for part in parts: 
            instance.parts.add(*part)         
        return redirect('moto_detail', pk=pk)

@method_decorator(login_required(login_url='/'), name='dispatch')
class RecordDelete(DeleteView):
    def post (self, request, pk):
        Record.objects.filter(pk=pk).delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))

@method_decorator(login_required(login_url='/'), name='dispatch')
class RecordUpdate(UpdateView):
    model = Record
    fields = ['description']
    template_name = 'record_update.html'

    def get_success_url(self):
        return reverse('moto_detail', kwargs={'pk': self.object.motorcycle.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        record = Record.objects.get(pk=self.object.pk)
        context['parts'] = Part.objects.exclude(id__in=record.parts.all().values_list('id'))
        return context 
    
""" 
Part 
"""
@method_decorator(login_required(login_url='/'), name='dispatch')
class PartsList(CreateView):
    model = Part
    fields = ['part_number', 'description']
    template_name = 'parts_list.html'
        
    def post(self, request):
        num = request.POST.get('part_number')
        des = request.POST.get('description')
        Part.objects.create(part_number=num, description=des)
        return redirect('parts_list')
### Parts Search 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pn = self.request.GET.get('pn')
        context["header"] = 'Search by Part Number'
        
        if pn == None:
            context['results'] = Part.objects.all()
            context['header'] = 'Displaying all parts in database' 
        if pn != None: 
            context['results'] = Part.objects.filter(part_number__icontains=pn)
            context["header"] = f'{pn}'
            return context
        else: 
            return context

@method_decorator(login_required(login_url='/'), name='dispatch')   
class RecordPartAssoc(View): 

    def get(self, request, pk, part_pk):
        assoc = request.GET.get('assoc')

        if assoc == 'remove':
            Record.objects.get(pk=pk).parts.remove(part_pk)
        if assoc == 'add':
            Record.objects.get(pk=pk).parts.add(part_pk)

        return redirect('record_update', pk=pk)



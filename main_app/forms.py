
from django.forms import EmailField, IntegerField,ModelMultipleChoiceField, CheckboxSelectMultiple, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from .models import Client, Record, Tech, Part

class SignUpFormClient(UserCreationForm):
    email = EmailField(help_text='Please use a valid email address')

    class Meta:
        model= Client
        fields = ('username', 'email', 'first_name', 'last_name', 'address', 'phone', 'password1', 'password2')

class SignUpFormTech(UserCreationForm):
    email = EmailField(help_text='Please use a valid email address')

    class Meta:
        model = Tech
        fields = ('username', 'email', 'first_name', 'last_name', 'rate', 'password1', 'password2')

class CreateRecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['mileage', 'description', 'parts']
        
    mileage = IntegerField()
    description = TextInput()
    parts = ModelMultipleChoiceField(queryset=Part.objects.all(), widget=CheckboxSelectMultiple)
    

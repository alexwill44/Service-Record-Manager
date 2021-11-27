
from django.forms import EmailField
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Tech

class SignUpFormClient(UserCreationForm):
    email = EmailField(help_text='Please use a valid email address')

    class Meta:
        model= Client
        fields = ('username', 'email', 'first_name', 'last_name', 'address', 'phone', 'password1', 'password2')

class SignUpFormTech(UserCreationForm):
    email = EmailField(help_text='Please use a valid email address')

    class Meta:
        model= Tech
        fields = ('username', 'email', 'first_name', 'last_name', 'rate', 'password1', 'password2')


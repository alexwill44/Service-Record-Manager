from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register([Motorcycle, Client, Tech, Record, Part])
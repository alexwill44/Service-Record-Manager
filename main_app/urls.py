from django.urls import path
from . import views 
from .views import Home, About, SearchMoto

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('motorcycles/', SearchMoto.as_view(), name='moto_show')
]

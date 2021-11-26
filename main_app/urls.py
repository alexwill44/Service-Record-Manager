from django.urls import path
from . import views 
from .views import Home, About, MotoShow, MotoDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('motorcycles/', MotoShow.as_view(), name='moto_show'),
    path('motorcycles/<int:pk>/', MotoDetail.as_view(), name='moto_detail'), 
]
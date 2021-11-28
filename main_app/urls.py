from django.urls import path
from . import views 
from .views import Home, About, MotoCreate, MotoDetail, MotoDelete, RecordCreate

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('motorcycles/', MotoCreate.as_view(), name='moto_show'),
    path('motorcycles/<int:pk>/', MotoDetail.as_view(), name='moto_detail'),
    path('motorcycle/<int:pk>/delete/', MotoDelete.as_view(), name='moto_delete'),
    path('motorcycle/<int:pk>/record/new', RecordCreate.as_view(), name='record_create')
]
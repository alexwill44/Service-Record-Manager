from django.urls import path
from . import views 
from .views import Home, About, MotoCreate, MotoDetail, MotoDelete, RecordCreate, RecordDelete, RecordUpdate, PartsList

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('motorcycles/', MotoCreate.as_view(), name='moto_show'),
    path('motorcycle/<int:pk>/', MotoDetail.as_view(), name='moto_detail'),
    path('motorcycle/<int:pk>/delete/', MotoDelete.as_view(), name='moto_delete'),
    path('motorcycle/<int:pk>/<int:user_pk>/', RecordCreate.as_view(), name='record_create'),
    path('motorcycle/record/<int:pk>/delete/', RecordDelete.as_view(), name='record_delete'),
    path('motorcycle/record/<int:pk>/update/', RecordUpdate.as_view(), name='record_update'),
    path('parts/', PartsList.as_view(), name='parts_list')
]
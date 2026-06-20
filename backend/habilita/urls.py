from django.urls import path
from . import views

app_name = 'habilita'

urlpatterns = [
    path('', views.home, name='home'),
    path('aulas/', views.listar_aulas, name='listar_aulas'),
    path('cadastro/', views.cadastro, name='cadastro'),
    
]

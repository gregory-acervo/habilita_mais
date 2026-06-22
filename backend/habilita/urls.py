from django.urls import path
from . import views

app_name = 'habilita'

urlpatterns = [
    path('', views.home, name='home'),
    path('aulas/', views.listar_aulas, name='listar_aulas'),
    path('login/', views.login_cliente, name='login_cliente'),
    path('cadastro/', views.cadastrar_cliente, name='cadastrar_cliente'),
    
]
1
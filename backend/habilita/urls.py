from django.urls import path
from . import views

app_name = 'habilita'

urlpatterns = [
    path('cliente/meus_agendamentos/', views.meus_agendamentos, name='meus_agendamentos'),  
    path('cliente/agendamento/', views.agendamento, name='agendamento'),  
    path('cadastro/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('cliente/', views.cliente_home, name='cliente_home'),
    path('login/', views.login_cliente, name='login_cliente'),
    path('aulas/', views.listar_aulas, name='listar_aulas'),
    path('', views.index, name='index'),
]

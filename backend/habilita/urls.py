from django.urls import path
from . import views

app_name = 'habilita'

urlpatterns = [
    path('', views.listar_aulas, name='listar_aulas'),
]
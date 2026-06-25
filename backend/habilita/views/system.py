from django.shortcuts import render, get_object_or_404
from ..models import AulaTeorica, AulaPratica, ExameTeorico, ExamePratico
from calendar import HTMLCalendar

def cliente_home(request):
    return render(request, 'habilita/cliente/home.html')

def agendamento(request, year, month):
    month_number = int()
    calendar = HTMLCalendar().formatmonth(year, month)
    return render(request, 'habilita/cliente/agendamento.html', {'calendar': calendar})

def meus_agendamentos(request):
    return render(request, 'habilita/cliente/meus_agendamentos.html')    

def listar_aulas(request):
    aulas = AulaTeorica.objects.all, AulaPratica.objects.all()
    context = {'aulas': aulas}
    #return render (request, '', context)
    
def listar_exames(request):
    exames = ExameTeorico.objects.all, ExamePratico.objects.all()
    context = {'exames': exames}
    #return render (request, '', context)
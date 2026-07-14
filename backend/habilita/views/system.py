from django.shortcuts import render, get_object_or_404
import datetime
from ..models import AulaTeorica, AulaPratica, ExameTeorico, ExamePratico
from calendar import HTMLCalendar

def cliente_home(request):
    return render(request, 'habilita/cliente/home.html')

def agendamento(request, year=None, month=None):
    # Se ano ou mês não forem passados, usa a data de hoje
    hoje = datetime.date.today()
    if year is None:
        year = hoje.year
    if month is None:
        month = hoje.month

    # Gera o calendário com os inteiros recebidos
    calendar = HTMLCalendar().formatmonth(year, month)
    return render(request, 'habilita/cliente/agendamento.html', {'calendar': calendar})

def meus_agendamentos(request):
    # Pega o ano e mês atuais
    hoje = datetime.date.today()
    calendar = HTMLCalendar().formatmonth(hoje.year, hoje.month)
    
    # Envia o calendário no contexto
    return render(request, 'habilita/cliente/meus_agendamentos.html', {'calendar': calendar}) 

def listar_aulas(request):
    aulas = AulaTeorica.objects.all(), AulaPratica.objects.all()
    context = {'aulas': aulas}
    #return render (request, '', context)
    
def listar_exames(request):
    exames = ExameTeorico.objects.all, ExamePratico.objects.all()
    context = {'exames': exames}
    #return render (request, '', context)
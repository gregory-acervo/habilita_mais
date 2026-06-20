from django.shortcuts import render, get_object_or_404
from ..models import AulaTeorica, AulaPratica, ExameTeorico, ExamePratico

def listar_aulas(request):
    aulas = AulaTeorica.objects.all, AulaPratica.objects.all()
    context = {'aulas': aulas}
    #return render (request, '', context)
    
def listar_exames(request):
    exames = ExameTeorico.objects.all, ExamePratico.objects.all()
    context = {'exames': exames}
    #return render (request, '', context)
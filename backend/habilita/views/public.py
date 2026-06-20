from django.shortcuts import render

#Views para as páginas públicas

def home(request):
    return render(request, 'habilita/index.html')

def cadastro(request):
    return render(request, 'habilita/cadastro.html')
 
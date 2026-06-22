from django.shortcuts import render

# View para a página pública
def home(request):
    return render(request, 'habilita/index.html')
 
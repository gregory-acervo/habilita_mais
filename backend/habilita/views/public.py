from django.shortcuts import render

# View para a página pública
def index(request):
    return render(request, 'habilita/index.html')
 
from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms import ClienteForm


def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('habilita:cliente_home')
        messages.error(request, 'Erro ao cadastrar. Verifique os dados abaixo.')
    else:
        form = ClienteForm()

    return render(request, 'habilita/cadastro.html', {'form': form})




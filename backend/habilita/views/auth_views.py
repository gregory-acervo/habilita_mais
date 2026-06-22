from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from ..models import Cliente
from ..forms import LoginForm

def login_cliente(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            try:
                cliente = Cliente.objects.get(email=email, ativo=True)
                
                if check_password(senha, cliente.senha):
                    request.session['cliente_id'] = cliente.id
                    messages.success(request,f"Bem-vindo de volta, {cliente.nome}!]")
                    return redirect('loja:home')
                else:
                    messages.error(request, "Senha incorreta.")
            except Cliente.DoesNotExist:
                messages.error(request, "Email não encontrado ou conta desativada.")
    else:
        form = LoginForm()

    return render(request, 'habilita/login.html', {'form': form, 'titulo_aba': 'Login'})



"""Função logout_client
Encerra a sessão do cliente, removendo o seu ID.
"""
def logout_cliente(request):
	if 'cliente_id' in request.session:
		del request.session['cliente_id']
		messages.success(request, "Você saiu com sucesso.")
	return redirect('habilita:index')


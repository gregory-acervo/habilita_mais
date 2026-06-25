from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Cliente
from ..forms import ClienteEditForm

def checar_sessao(request):
    
    cliente_id = request.session.get('cliente_id')
    if cliente_id:
    
        return Cliente.objects.filter(id=cliente_id, ativo=True).first()
    return None

def editar_perfil(request):
    cliente = checar_sessao(request)
    
    # Portanto é raro se não tiver logado, manda pra login
    if not cliente:
        messages.warning(request, "Faça login para acessar seu perfil.")
        return redirect('habilita:login_cliente')
    
    if request.method == 'POST':
        # Nessa parte é um UPDATE, não um CREATE
        form = ClienteEditForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Seus dados foram atualizados com sucesso!")
            return redirect('habilita:editar_perfil')
    else:
        # Preenche o formulário com os dados atuais do banco
        form = ClienteEditForm(instance=cliente)
    
    content = {'form': form,
               'cliente': cliente,
               'titulo_aba': 'Meu Perfil'
               }
    
    return render(request, 'habilita/perfil.html', content)

def deletar_conta(request):
    cliente = checar_sessao(request)
    if not cliente:
        return redirect('habilita:login_cliente')
    
    if request.method == 'POST':
        # DELEÇÃO LÓGICA: Apenas atualizamos o status
        cliente.ativo = False
        cliente.save()
        
        # Fazemos o logout do usuário
        del request.session['cliente_id']
        messages.success(request, "Sua conta foi desativada com sucesso.")
        return redirect('habilita:cliente_home')
    
    return render(request, 'habilita/confirmar_delecao.html', {'cliente': cliente})

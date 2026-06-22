from django import forms
from .models import Cliente
from django.contrib.auth.hashers import make_password


class ClienteForm(forms.ModelForm):
    # 1. Campo extra que existe apenas no formulário HTML para validação
    confirmar_senha = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme sua senha'
        })
    )

    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'email', 'telefone', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome completo'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'usuario@email.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000'
            }),
            'senha': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Crie uma senha'
            }),
        }

    # 3. Método de validação limpa que compara os campos e aplica o hash
    def clean(self):
        cleaned_data = super().clean()

        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha and confirmar_senha:
            if senha != confirmar_senha:
                raise forms.ValidationError('As senhas não conferem. Digite novamente.')
            cleaned_data['senha'] = make_password(senha)

        return cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'seu@email.com'
        })
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Sua senha'
        })
    )


class ClienteEditForm(forms.ModelForm):
    class Meta:
        model = Cliente
        # Excluímos 'cpf' e 'senha' da edição básica
        fields = ['nome', 'email', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }
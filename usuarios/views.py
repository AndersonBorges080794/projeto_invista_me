from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def novo_usuario(request):
    #tipo, validar, informar, salvar.
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)#Passando as informações da requisição para classe  UserRegisterForm().
        if formulario.is_valid():#validando o formulário da requisição.
            formulario.save()#salvando o formulário no banco de dados
            usuario = formulario.cleaned_data.get('username')#Pegando o username na requisição.
            messages.success(request, f'O usuario {usuario} foi criado com sucesso!')#Exibindo a mensagem para o usuário.
            return redirect('login')#Direcionando para a pagina inicial(listar_investimentos).

    else:
        formulario = UserRegisterForm()#Criando um formulário vazio pois não estamos passando o parâmetro "request.POST"
    
    return render(request, 'usuarios/registrar.html', {'formulario': formulario})


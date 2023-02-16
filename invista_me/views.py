from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required



# def pagina_inicial(request):
#     return HttpResponse('Pronto para investir')

# def pagina_contato(request):
#     return HttpResponse('Pagina de contato')


# def minha_historia(request):
#     pessoa = {
#         "nome": "Anderson",
#         "idade": 28,
#         "hobby": 'games'
#     }
#     #Passando informações(nesse caso foi um dicinário mas em uma aplicação real será puxado de um banco de dados) 
#     #para uma pagina html.
#     return render(request, 'investimentos/minha_historia.html', pessoa)


#
# def investimento_registrado(request):
#     investimento = {
#         'tipo_investimento': request.POST.get('TipoInvestimento')#Aqui estamos recuperando os dados enviado pelo form do arquivo "novo_investimento.html"
#     }

#     #Passando informações para uma pagina html.
#     return render(request, 'investimentos/investimento_registrado.html', investimento)


#Função que vai pegar as informações passada pelo usuário
# def novo_investimento(request):
#     return render(request, 'investimentos/novo_investimento.html')


#Função que vai listar todos os investimentos no index
def listar_investimentos(request):
    dados = {
        'dados': Investimento.objects.all()#Indo até a classe Investimento, pegando todos os objetos e todos os registros
    }
    return render(request, 'investimentos/listar_investimentos.html', context=dados)


#Função que vai exibir um investimento por id
def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)#Indo até a classe Investimento, pegando todos os objetos e recuperando o registro aplicando filtro utilizando pk(chave primária mas pode ser qualquer filtro).
    }
    return render(request, 'investimentos/detalhe.html', dados)


#Função que vai pegar as informações passada pelo usuário e criar um investimento
@login_required#Esse decoret tem a função de bloquear a funcionalidade/rota para usuários que não estejam logados.
def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)#Pegando os dados do form da requisição.
        if investimento_form.is_valid():#Verificando se os dados do form da requisição são válidos.
            investimento_form.save()#Salvando os dados da requisição no banco de dados.
        return redirect('listar_investimentos')#Redireciona para o template selecionado.
    else:   
        investimento_form = InvestimentoForm()#Instânciando a classe InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)
    
    
#Função que vai editar dados existentes.
@login_required#Esse decoret tem a função de bloquear a funcionalidade/rota para usuários que não estejam logados.
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)#Indo até a classe Investimento, pegando todos os objetos e recuperando o registro aplicando filtro utilizando pk(chave primária mas pode ser qualquer filtro).
    
    #Verificar se é o método GET
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)#Populando o nosso formulário com os dados recuperados do banco.
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})#Podemos também criar um dicionário direto no return.
    #Caso a requisição seja um POST
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('listar_investimentos')
    

#Função que vai excluir dados existentes.
@login_required#Esse decoret tem a função de bloquear a funcionalidade/rota para usuários que não estejam logados.
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':#Aqui é post pois estamos mandando dados na requisição para exclusão.
        investimento.delete()#Aqui estamos excluído de fato os dados anviados na requisição no banco de dados.
        return redirect('listar_investimentos')
    
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})
from django.shortcuts import render, redirect
from  core.forms import FormCliente, FormFabricante, FormVeiculo, FormTabela, FormRotativo, FormMensalista
from core.models import Cliente, Fabricante, Veiculo, Tabela, Rotativo, Mensalista
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return render(request, 'core/index.html')

class Registrar(generic.CreateView):
    template_name = 'registration/register.html'
    success_url = '/'
    form_class = UserCreationForm


@login_required()
def cadastro_cliente(request):
    if request.user.is_staff:
        form  = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_lista_clientes')
        contexto = {'form':form, 'titulo': 'Cadastro de Cliente','stringBotao': 'Cadastrar','url':'/'}
        return render(request, 'core/cadastro.html', contexto)
    else:
        contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
        return render(request, 'core/mensagem.html', contexto)

@login_required()
def lista_clientes(request):
    if request.user.is_staff:
        dados = Cliente.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/lista_clientes.html', contexto)
    else:
        contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
        return render(request, 'core/mensagem.html', contexto)

@login_required()
def altera_cliente(request, id):
    if request.user.is_staff:
        objeto = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=objeto)
        form.fields['email'].widget.attrs['readonly'] = True
        if form.is_valid():
            form.save()
            return render(request,'core/mensagem.html',{'string': f'Dados de {objeto.nome} salvos!', 'url':'/lista_clientes/'})
        contexto = {'form':form,'titulo':'Altera', 'stringBotao': 'Salvar', 'url':'/lista_clientes/',
                    'formAtualiza': True}
        return render(request, 'core/cadastro.html', contexto)
    else:
            contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
            return render(request, 'core/mensagem.html', contexto)

@login_required()
def exclua_cliente(request, id):
    if request.user.is_staff:
        objeto = Cliente.objects.get(id=id)
        if request.POST:
            objeto.delete()
            return redirect('url_lista_clientes')
        contexto = {'objeto':objeto.nome, 'url': '/lista_clientes'}
        return render(request,'core/confirma_exclusao.html',contexto)
    else:
            contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
            return render(request, 'core/mensagem.html', contexto)

@login_required()
def lista_veiculos(request):
     if request.user.is_staff:
        dados = Veiculo.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/lista_veiculos.html', contexto)
     else:
        contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
        return render(request, 'core/mensagem.html', contexto)

@login_required()
def cadastro_veiculo(request):
    if request.user.is_staff:
        form = FormVeiculo (request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_lista_veiculos')
        contexto = {'form':form,  'titulo': 'Cadastro de Veiculos','stringBotao': 'Cadastrar','url':'/'}
        return render(request, 'core/cadastro.html', contexto)
    else:
            contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
            return render(request, 'core/mensagem.html', contexto)

@login_required()
def altera_veiculo(request, id):
    if request.user.is_staff:
        objeto = Veiculo.objects.get(id = id)
        form = FormVeiculo(request.POST or None, request.FILES or None, instance=objeto)
        #form.fields['id_cliente'].widget.attrs['readonly'] = True
        #form.fields['id_fabricante'].widget.attrs['readonly'] = True
        contexto = {'form': form,'string': f'Dados de {objeto.modelo} salvos!','stringBotao': 'Salvar', 'url':'/lista_veiculos/',
                    'formAtualiza': True}
        if form.is_valid():
            form.save()
            return render(request, 'core/mensagem.html', contexto)
        return render(request, 'core/cadastro.html', contexto)
    else:
            contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
            return render(request, 'core/mensagem.html', contexto)

@login_required()
def exclua_veiculo(request, id):
    if request.user.is_staff:
        objeto = Veiculo.objects.get(id = id)
        #se veiculo por request POST o usuario clicou em 'sim'
        if request.POST:
            objeto.delete()
            return redirect('url_lista_veiculos')
        contexto = {'objeto':objeto.modelo, 'url':'/lista_veiculos'}
        return render(request,'core/confirma_exclusao.html',contexto)
    else:
            contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
            return render(request, 'core/mensagem.html', contexto)

@login_required()
def cadastro_fabricante(request):
    if request.user.is_staff:
        form = FormFabricante(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('url_lista_fabricantes')
        contexto = {'form': form,  'titulo': 'Cadastro de Fabricante','stringBotao': 'Cadastrar','url':'/'}
        return render(request,'core/cadastro.html', contexto)
    else:
            contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
            return render(request, 'core/mensagem.html', contexto)

@login_required()
def lista_fabricantes(request):
    if request.user.is_staff:
        dados = Fabricante.objects.all()
        contexto = {'dados': dados}

        return render(request,'core/lista_fabricantes.html', contexto)
    else:
            contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
            return render(request, 'core/mensagem.html', contexto)

@login_required()
def altera_fabricante(request, id):
    if request.user.is_staff:
       objeto = Fabricante.objects.get(id = id)
       form = FormFabricante(request.POST or None, request.FILES or None, instance=objeto)
       contexto = {'form': form,'stringBotao': 'Salvar', 'url':'/lista_fabricantes/',
                   'formAtualiza': True}
       if form.is_valid():
            form.save()
            return render(request, 'core/mensagem.html', {'string': f'Dados de {objeto.descricao} alterados!'})
       return render(request, 'core/cadastro.html', contexto)
    else:
            contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!'}
            return render(request, 'core/mensagem.html', contexto)

@login_required()
def exclua_fabricante(request, id):
    if request.user.is_staff:
        objeto = Fabricante.objects.get(id = id)
        if request.POST:
            objeto.delete()
            return redirect('url_lista_fabricantes')
        contexto = {'objeto':objeto.descricao, 'url':'/lista_fabricantes'}
        return render(request,'core/confirma_exclusao.html',contexto)
    else:
            contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
            return render(request, 'core/mensagem.html', contexto)

@login_required()
def cadastro_tabelas(request):
    if request.user.is_staff:
        form  = FormTabela (request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('url_lista_tabelas')
        contexto = {'form':form, 'titulo': 'Cadastro Tabela','stringBotao': 'Cadastrar','url':'/'}
        return render(request, 'core/cadastro.html', contexto)
    else:
            contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
            return render(request, 'core/mensagem.html', contexto)

@login_required()
def lista_tabelas(request):

    dados = Tabela.objects.all()
    contexto = {'dados': dados}
    return render(request, 'core/lista_tabelas.html', contexto)


@login_required()
def altera_tabelas(request, id):
    if request.user.is_staff:
       objeto = Tabela.objects.get(id = id)
       form = FormTabela(request.POST or None,  instance=objeto)
       contexto = {'form': form,'stringBotao': 'Salvar', 'url':'/lista_tabelas/',
                   'formAtualiza': True}
       if form.is_valid():
            form.save()
            return render(request, 'core/mensagem.html', {'string': f'Dados de {objeto.descricao} salvos!'})
       return render(request, 'core/cadastro.html', contexto)
    else:
            contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!'}
            return render(request, 'core/mensagem.html', contexto)

@login_required()
def exclua_tabelas(request, id):
    if request.user.is_staff:
        objeto = Tabela.objects.get(id = id)
        if request.POST:
            objeto.delete()
            return redirect('url_lista_tabelas')
        contexto = {'objeto':objeto.descricao, 'url':'/lista_tabelas'}
        return render(request,'core/confirma_exclusao.html',contexto)
    else:
            contexto = {'string' : 'Você não tem permissão para executar esta operação. Procure seu Administrador!', 'url':'/'}
            return render(request, 'core/mensagem.html', contexto)

def cadastro_rotativo(request):
        form  = FormRotativo(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('url_lista_rotativo')
        contexto = {'form':form, 'titulo': 'Cadastro de Rotativo','stringBotao': 'Cadastrar',
                    'dateTime': True}
        return render(request, 'core/cadastro.html', contexto)

def lista_rotativo(request):

    dados = Rotativo.objects.all()
    contexto = {'dados': dados}

    return render(request,'core/lista_rotativo.html', contexto)

def atualiza_rotativo(request, id):
        obj = Rotativo.objects.get(id=id)
        form  = FormRotativo(request.POST or None, instance=obj)
        if form.is_valid():
            obj.calcula_total()
            form.save()
            return redirect('url_lista_rotativo')
        contexto = {'form':form, 'titulo': 'Atualiza Rotativo','stringBotao': 'Atualizar',
                    'dateTime': True, 'formAtualiza': True}
        return render(request, 'core/cadastro.html', contexto)

def exclua_rotativo(request, id):
        objeto = Rotativo.objects.get(id = id)
        if request.POST:
            objeto.delete()
            return redirect('url_lista_rotativo')
        contexto = {'objeto':objeto.id_Veiculo, 'url':'/lista_rotativo'}
        return render(request,'core/confirma_exclusao.html',contexto)

def cadastro_mensalista(request):
        form  = FormMensalista(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('url_lista_mensalista')
        contexto = {'form':form, 'titulo': 'Cadastro de Mensalista','stringBotao': 'Cadastrar','url':'/'}
        return render(request, 'core/cadastro.html', contexto)

def lista_mensalista(request):

    dados = Mensalista.objects.all()
    contexto = {'dados': dados}

    return render(request,'core/lista_mensalista.html', contexto)

def atualiza_mensalista(request, id):
        obj = Mensalista.objects.get(id=id)
        form  = FormMensalista(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('url_lista_mensalista')
        contexto = {'form':form, 'titulo': 'Atualiza Mensalista','stringBotao': 'Atualizar',
                    'formAtualiza': True}
        return render(request, 'core/cadastro.html', contexto)

def exclua_mensalista(request, id):
        objeto = Mensalista.objects.get(id = id)
        if request.POST:
            objeto.delete()
            return redirect('url_lista_mensalista')
        contexto = {'objeto':objeto.id_Veiculo, 'url':'/lista_mensalista'}
        return render(request,'core/confirma_exclusao.html',contexto)





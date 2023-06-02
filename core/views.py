from http import client
from django.shortcuts import render, redirect
from core.forms import FormCliente, FormVeiculo, FormMarca, FormTabela, FormMensalista, FormRotativo
from core.models import Cliente, Marca, Veiculo, Tabela, Mensalista, Rotativo
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal')
    template_name = 'registration/registrar.html'

def home(request):
    contexto = {'home': 'home'}
    return render(request, 'core/index.html', contexto)

@login_required
def cadastroClientes(request):
    if request.user.is_staff:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form' : form, 'titulo_pagina': 'Cad_Cliente', 'txt_nome_pagina': 'Cadastro de Cliente', 'home': 'home'}
        return render(request, 'cadastros/cadastro.html', contexto)
    return render(request, 'aviso.html')

@login_required
def cadastroVeiculos(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('url_principal')
    contexto = {'form' : form, 'titulo_pagina': 'Cad_Veiculo', 'txt_nome_pagina': 'Cadastro de Veiculo', 'home': 'home'}
    return render(request, 'cadastros/cadastro.html', contexto)

@login_required
def listaClientes(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Cliente.objects.filter(nome__contains = request.POST['input_pesquisa'])
        else:
            dados = Cliente.objects.all()
        contexto = {'dados': dados, 'text_input':'Digite o nome do cliente'}
        print(contexto)
        return render(request, 'listagem/listagemCliente.html', contexto)
    return render(request, 'aviso.html')

@login_required
def listaVeiculo(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Veiculo.objects.filter(placa__contains = request.POST['input_pesquisa'])
        else:
            dados = Veiculo.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite a placa do veículo'}
        return render(request, 'listagem/listagemVeiculo.html', contexto)
    return render(request, 'aviso.html')

@login_required
def listaMarca(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Marca.objects.filter(marca__contains = request.POST['input_pesquisa'])    
        else:
            dados = Marca.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite o nome da marca'}
        return render(request, 'listagem/listagemMarca.html', contexto)

@login_required
def tabela(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Tabela.objects.filter(valor__contains = request.POST['input_pesquisa'])    
        else:
            dados = Tabela.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite o valor da tabela'}
        return render(request, 'listagem/listagemTabela.html', contexto)
    return render(request, 'aviso.html')

@login_required
def listaMensalista(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Mensalista.objects.filter(veiculo_id__placa__contains = request.POST['input_pesquisa'])    
        else:
            dados = Mensalista.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite a placa do veiculo'} 
        return render(request, 'listagem/listagemMensalista.html', contexto)
    return render(request, 'aviso.hmtl')
    
@login_required
def listaRotativo(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Rotativo.objects.filter(veiculo_id__placa__contains = request.POST['input_pesquisa'])    
        else:
            dados = Rotativo.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite a placa do veiculo'}
        return render(request, 'listagem/listagemRotativos.html', contexto)
    return render(request, 'aviso.hmtl')

@login_required
def cadastroTabela(request):
    if request.user.is_staff:
        form = FormTabela(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')

    contexto = {'form' : form, 'titulo_pagina': 'Cad_Tabela', 'txt_nome_pagina': 'Cadastro de Tabela', 'home': 'home'}
    return render(request, 'cadastros/cadastro.html', contexto)

@login_required
def cadastroMarca(request):
    if request.user.is_staff:
        form = FormMarca(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
    
    contexto = {'form': form, 'titulo_pagina':'Cad_Marca', 'txt_nome_pagina': 'Cadastrar Marca', 'home': 'home'}
    return render (request, 'cadastros/cadastro.html', contexto)

@login_required
def cadastrosMensalista(request):
    if request.user.is_staff:
        form = FormMensalista(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')

    contexto = {'form': form, 'titulo_pagina': 'Cad_Mensa', 'txt_nome_pagina': 'Cadastro Mensalidade', 'home': 'home'}
    return render(request, 'cadastros/cadastro.html', contexto)

@login_required
def cadastrosRotativos(request):
    if request.user.is_staff:
        form = FormRotativo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        
    contexto = {'form': form, 'titulo_pagina':"Cad_Rotativo", 'txt_nome_pagina':'Cadastros de Rotativos', 'home': 'home'}
    return render(request, 'cadastros/cadastro_rotativo_dividido.html', contexto)

@login_required
def alterar_marca(request, id):
    if request.user.is_staff:
        obj = Marca.objects.get(id = id)
        form = FormMarca(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_listaMarca')
    
    contexto = {'form': form, 'titulo_pagina': 'alter_Marca', 'txt_nome_pagina': 'Atualização de Marca', 'home': 'home'}
    return render(request, 'cadastros/cadastro.html', contexto)

def altera_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id = id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_listaClientes')
    
    contexto = {'form': form, 'titulo_pagina': 'Alter_Perfil', 'txt_nome_pagina': 'Atualização de Perfil', 'home': 'home'}
    return render(request, 'cadastros/cadastro.html', contexto)

def altera_veiculo(request, id):
    if request.user.is_staff:
        obj = Veiculo.objects.get(id = id)
        form = FormVeiculo(request.POST or None, request.FILES or None, instance=obj)

        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_listaVeiculo')
    
    contexto = {'form': form, 'titulo_pagina': 'Altera_veiculo', 'txt_nome_pagina': 'Atualização Veiculo', 'home': 'home'}
    return render(request, 'cadastros/cadastro.html', contexto)

def altera_tabela(request, id):
    if request.user.is_staff:
        obj = Tabela.objects.get(id = id)
        form = FormTabela(request.POST or None, request.FILES or None, instance=obj)

        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_tabela')
    
    contexto = {'form': form, 'titulo_pagina': 'Alterar_Tabelar', 'txt_nome_pagina': 'Editar Tabela', 'home': 'home'}
    return render(request, 'cadastros/cadastro.html', contexto)

def alterar_rotativo(request, id):
    if request.user.is_staff:
        obj = Rotativo.objects.get(id = id)
        form = FormRotativo(request.POST or None, request.FILES or None, instance=obj)

        if request.POST:
            if form.is_valid():
                obj.calculo_total()
                form.save()
            return redirect('url_listaRotativo')
    
    contexto = {'form': form, 'titulo_pagina': 'Alterar_Rotativo', 'txt_nome_pagina': 'Editar Rotativo', 'home': 'home'}
    return render(request, 'cadastros/cadastro_rotativo_dividido.html', contexto)

def alterar_mensalista(request, id):
    if request.user.is_staff:
        obj = Mensalista.objects.get(id = id)
        form = FormMensalista(request.POST or None, request.FILES or None, instance=obj)

        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_listaMensalista')
    
    contexto = {'form': form, 'titulo_pagina': 'Alterar_Mensalista', 'txt_nome_pagina': 'Editar Mensalista', 'home': 'home'}
    return render(request, 'cadastros/cadastro.html', contexto)



def exclui_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id = id)
        if request.POST:        
            obj.delete()
            contexto = {'txt_tipo': 'Cliente', 'txt_info': obj.nome, 'txt_url': '/listagemCliente'}
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto = {'txt_info': obj.nome}
            return render(request, 'excluir/confirma_exclusao.html', contexto)            

def excluir_veiculo(request, id):
    if request.user.is_staff:
        obj = Veiculo.objects.get(id = id)
        if request.POST:
            obj.delete()
            contexto = {'txt_tipo': 'Veiculo', 'txt_info': obj.modelo, 'txt_url':'/listagemVeiculo'}
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto = {'txt_info': obj.modelo, 'txt_url':'/listagemVeiculo'}
            return render(request, 'excluir/confirma_exclusao.html', contexto)

def excluir_tabela(request, id):
    if request.user.is_staff:
        obj = Tabela.objects.get(id = id)
        if request.POST:
            obj.delete()
            contexto = {'txt_tipo': 'Tabela', 'txt_info': obj.descricao, 'txt_url':'/tabela'}
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto = {'txt_info': obj.descricao}
            return render(request, 'excluir/confirma_exclusao.html', contexto)

def excluir_marca(request, id):
    if request.user.is_staff:
        obj = Marca.objects.get(id = id)
        contexto = {'txt_tipo': 'Marca', 'txt_info': obj.marca, 'txt_url':'/listagemMarca'}
        if request.POST:
            obj.delete()            
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto.update({'txt_info': obj.marca})
            return render(request, 'excluir/confirma_exclusao.html', contexto)
    
def excluir_rotativo(request, id):
    if request.user.is_staff:
        obj = Rotativo.objects.get(id = id)
        contexto = {'txt_tipo': 'Rotativo', 'txt_info': obj.veiculo_id, 'txt_url':'/listagemRotativo'}
        if request.POST:
            obj.delete()            
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto.update({'txt_info': obj.veiculo_id})
            return render(request, 'excluir/confirma_exclusao.html', contexto)
    
def excluir_mensalista(request, id):
    if request.user.is_staff:
        obj = Mensalista.objects.get(id = id)
        contexto = {'txt_tipo':'Mensalista', 'txt_info': obj.veiculo_id, 'txt_url': '/listagemMensalista'}

        if request.POST:
            obj.delete()            
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            contexto.update({'txt_info': obj.veiculo_id})
            return render(request, 'excluir/confirma_exclusao.html', contexto)
    
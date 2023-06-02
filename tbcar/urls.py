"""tbcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import core.views as core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/registrar/', core.Registrar.as_view(), name='url_registrar'),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', core.home, name='url_principal'),
    path('cadastrosCliente/', core.cadastroClientes, name='url_cadastroClientes'),
    path('cadastroVeiculo/', core.cadastroVeiculos, name='url_cadastroVeiculo'),
    path('cadastroMarca/', core.cadastroMarca, name='url_cadastroMarca'),
    path('cadastrosMensalista', core.cadastrosMensalista, name='url_cadastrosMensalista'),  
    path('cadastroTabela/', core.cadastroTabela, name='url_cadastroTabela'),
    path('cadastroRotativo', core.cadastrosRotativos, name='url_cadastroRotativo'),
    path('listagemCliente/', core.listaClientes, name='url_listaClientes'),
    path('listagemVeiculo/', core.listaVeiculo, name='url_listaVeiculo'),
    path('listagemMarca/', core.listaMarca, name='url_listaMarca'),
    path('listagemMensalista', core.listaMensalista, name='url_listaMensalista'),
    path('listagemRotativo', core.listaRotativo, name='url_listaRotativo'),
    path('tabela/', core.tabela, name='url_tabela'),
    path('altera_cliente/<int:id>/', core.altera_cliente, name='url_altera_cliente'),
    path('altera_veiculo/<int:id>/', core.altera_veiculo, name='url_altera_veiculo'),
    path('altera_tabela/<int:id>/', core.altera_tabela, name='url_altera_tabela'),
    path('altera_marca/<int:id>/', core.alterar_marca, name='url_altera_marca'),
    path('alerar_rotativo/<int:id>', core.alterar_rotativo, name='url_alterar_rotativo'),
    path('alterar_mensalista/<int:id>', core.alterar_mensalista, name='url_alterar_mensalista'),
    path('excluir_cliente/<int:id>/', core.exclui_cliente, name='url_excluir_cliente'),
    path('excluir_veiculo/<int:id>/', core.excluir_veiculo, name='url_excluir_veiculo'),
    path('excluir_tabela/<int:id>/', core.excluir_tabela, name='url_excluir_tabela'),
    path('excluir_marca/<int:id>/', core.excluir_marca, name='url_excluir_marca'),
    path('excluir_rotativo/<int:id>', core.excluir_rotativo, name='url_excluir_rotativo'),
    path('excluir_mensalista/<int:id>', core.excluir_mensalista, name='url_excluir_mensalista')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

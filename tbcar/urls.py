"""tbcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('admin/', admin.site.urls),
    path('', home, name='url_principal'),
    path('cadastro_cliente/', cadastro_cliente, name="url_cadastro_cliente"),
    path('lista_clientes/', lista_clientes, name="url_lista_clientes"),
    path('cadastro_veiculo/', cadastro_veiculo, name="url_cadastro_veiculo"),
    path('lista_veiculos/', lista_veiculos, name="url_lista_veiculos"),
    path('cadastro_fabricante/', cadastro_fabricante, name="url_cadastro_fabricante"),
    path('lista_fabricantes/', lista_fabricantes, name="url_lista_fabricantes"),
    path('altera_cliente/<int:id>/', altera_cliente,name='url_altera_cliente'),
    path('exclua_cliente/<int:id>/', exclua_cliente, name='url_exclua_cliente'),
    path('altera_veiculo/<int:id>/', altera_veiculo, name='url_altera_veiculo'),
    path('exclua_veiculo/<int:id>/', exclua_veiculo, name='url_exclua_veiculo'),
    path('altera_fabricante/<int:id>/', altera_fabricante, name='url_altera_fabricante'),
    path('exclua_fabricante/<int:id>/', exclua_fabricante, name='url_exclua_fabricante'),
    path('cadastro_tabelas/', cadastro_tabelas, name="url_cadastro_tabelas"),
    path('lista_tabelas/', lista_tabelas, name="url_lista_tabelas"),
    path('altera_tabelas/<int:id>/', altera_tabelas, name='url_altera_tabelas'),
    path('exclua_tabelas/<int:id>/', exclua_tabelas, name='url_exclua_tabelas'),
    path('cadastro_rotativo/', cadastro_rotativo, name='url_cadastro_rotativo'),
    path('lista_rotativo/', lista_rotativo, name="url_lista_rotativo"),
    path('atualiza_rotativo/<int:id>/', atualiza_rotativo, name='url_atualiza_rotativo'),
    path('exclua_rotativo/<int:id>/', exclua_rotativo, name='url_exclua_rotativo'),
    path('cadastro_mensalista/', cadastro_mensalista, name='url_cadastro_mensalita'),
    path('lista_mensalista/', lista_mensalista, name="url_lista_mensalista"),
    path('atualiza_mensalista/<int:id>/', atualiza_mensalista, name='url_atualiza_mensalista'),
    path('exclua_mensalista/<int:id>/', exclua_mensalista, name='url_exclua_mensalista'),





]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

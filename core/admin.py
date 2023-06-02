from django.contrib import admin
from core.models import Marca, Cliente, Veiculo, Mensalista, Rotativo, Tabela
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Tabela)
admin.site.register(Mensalista)
admin.site.register(Rotativo)
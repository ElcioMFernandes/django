from django.contrib import admin
from .models import Cedente, Banco

class CedenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'razao_social', 'cnpj')
    list_display_links = ('id', 'razao_social')
    search_fields = ('razao_social', 'cnpj')
    list_per_page = 20

admin.site.register(Cedente, CedenteAdmin)

class BancoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnab')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'cnab')
    list_per_page = 20

admin.site.register(Banco, BancoAdmin)
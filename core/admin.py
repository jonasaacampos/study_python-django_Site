from django.contrib import admin
from .models import Cargo, Servico, Equipe, Funcionalidade


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ("cargo", "modificado", "ativo")


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "icon", "ativo", "modificado")


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ("nome", "cargo", "biografia", "modificado", "criado")


@admin.register(Funcionalidade)
class FuncionalidadeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "criado", "modificado", "ativo")

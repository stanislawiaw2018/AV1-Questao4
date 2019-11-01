from django.contrib import admin
from core.models import *
# default: "Administração do Django"
admin.site.site_header = 'Painel de Controle'
# default: "Administração do Site"
admin.site.index_title = 'Aplicações'
# default: ”Site de administração do Django"
admin.site.site_title = 'Emprestimo de Revista'

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = (
        'revista','data_emprestimo','data_devolucao','amigo'
    )

class RevistaAdmin(admin.ModelAdmin):
    list_display = (
        'numero_edicao','ano'
    )

class AmigoAdmin(admin.ModelAdmin):
    list_display =  (
        'nome','nome_mae','telefone'
    )
admin.site.register(Amigo)
admin.site.register(Revista)
admin.site.register(Emprestimo,EmprestimoAdmin)
admin.site.register(Caixa)
admin.site.register(Colecao)


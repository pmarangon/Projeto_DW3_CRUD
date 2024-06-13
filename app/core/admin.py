from django.contrib import admin
from core.models import Tarefa

class TarefaAdmin(admin.ModelAdmin):
  list_display = ('titulo', 'inicio', 'entrega', 'descricao', 'categoria')
  search_fields = ('entrega', 'titulo')


admin.site.register(Tarefa, TarefaAdmin)
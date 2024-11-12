from django.contrib import admin

from freitascodes.models import Imagens

@admin.register(Imagens)
class ImagensAdmin(admin.ModelAdmin):
  list_display = ['id','projeto','arquivo','ordem','descricao','ativo']
  search_fields = ['id','projeto','arquivo','descricao']
  autocomplete_fields = ['projeto',]
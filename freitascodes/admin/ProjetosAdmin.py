from django.contrib import admin

from freitascodes.models import Projetos, Imagens

class ImagensInline(admin.StackedInline):
  model = Imagens
  extra = 1

@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
  list_display = ['name','project_type','repo_name','avaliable_at','ativo']
  search_fields = ['name','project_type','repo_name','stacks']
  autocomplete_fields = ['stacks',]
  inlines = [ImagensInline]
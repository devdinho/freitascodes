from django.contrib import admin

from freitascodes.models import Projetos

@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
  list_display = ['name','project_type','repo_name','avaliable_at','ativo']
  search_fields = ['name','project_type','repo_name','stacks']
  autocomplete_fields = ['stacks',]
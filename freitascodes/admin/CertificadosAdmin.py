from django.contrib import admin

from freitascodes.models import Certificados

@admin.register(Certificados)
class CertificadosAdmin(admin.ModelAdmin):
  list_display = ['nome','avaliable_at','ativo']
  search_fields = ['nome','stacks']
  autocomplete_fields = ['stacks',]
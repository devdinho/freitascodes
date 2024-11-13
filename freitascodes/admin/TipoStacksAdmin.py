from django.contrib import admin

from freitascodes.models import TipoStacks, Stacks
class StacksInline(admin.StackedInline):
  model = Stacks
  extra = 1

@admin.register(TipoStacks)
class TipoStacksAdmin(admin.ModelAdmin):
  list_display = ['name',]
  search_fields = ['name',]
  inlines = [StacksInline]
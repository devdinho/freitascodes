from django.contrib import admin

from freitascodes.models import Stacks

@admin.register(Stacks)
class StacksAdmin(admin.ModelAdmin):
  list_display = ['name','stack_type','skillicon_name']
  search_fields = ['name','stack_type','skillicon_name']
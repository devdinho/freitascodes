from django.db import models

class TipoStacks(models.Model):
  name = models.CharField('Nome do Tipo', max_length=255)

  class Meta:
    verbose_name = 'Tipo de Stack'
    verbose_name_plural = 'Tipos de Stacks'
    ordering = ['name']
  
  def __str__(self):
    return f'{self.name}'
from django.db import models
from freitascodes.models import TipoStacks

class Stacks(models.Model):
  name = models.CharField('Nome da Tecnologia', max_length=255)
  stack_type = models.ForeignKey(TipoStacks, verbose_name='Tipo de Stack', default=1, on_delete=models.PROTECT)
  skillicon_name = models.CharField('Name do Skill Icon', help_text='Disponível em https://github.com/tandpfun/skill-icons?tab=readme-ov-file#icons-list')

  class Meta:
    verbose_name = 'Stack'
    verbose_name_plural = 'Stacks'
    ordering = ['stack_type','name']
    
  def __str__(self):
    return f'{self.name} ({self.skillicon_name}) - {self.stack_type}'
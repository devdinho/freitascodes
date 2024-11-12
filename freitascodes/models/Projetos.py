from django.db import models
from freitascodes.models import Stacks

PROJECT_TYPE_CHOICES = (
  (1,'Projeto'),    
  (2,'Biblioteca'),  
)

class Projetos(models.Model):
  name = models.CharField('Nome do Projeto', max_length=255)
  project_type = models.IntegerField('Tipo de Projeto', choices=PROJECT_TYPE_CHOICES, default=1)
  repo_name = models.CharField('Name do Repositório', help_text='Link do Github', max_length=500)
  avaliable_at = models.CharField('Disponível em', help_text='Link do Projeto em produção ou biblioteca no PYPI por exemplo.', max_length=500)

  stacks = models.ManyToManyField(Stacks, verbose_name='Stacks', help_text='Stacks utilizadas ou disponível para estas stacks')
  
  ativo = models.BooleanField(verbose_name='Está Disponível?', default=True)

  class Meta:
    verbose_name = 'Projeto'
    verbose_name_plural = 'Projetos'
    ordering = ['project_type','name']
  
  def __str__(self):
    return f'{self.name} ({self.repo_name})'
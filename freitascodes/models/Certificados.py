from django.db import models
from freitascodes.models import Stacks

class Certificados(models.Model):
  nome = models.CharField('Name do Repositório', help_text='Link do Github', max_length=500)
  descricao = models.TextField('Descrição do Curso/Certificado')

  avaliable_at = models.CharField('Disponível em', help_text='Link do Projeto em produção ou biblioteca no PYPI por exemplo.', max_length=2000)
  arquivo = models.FileField('Arquivo', upload_to="certificados", null=True, blank=True)
  stacks = models.ManyToManyField(Stacks, verbose_name='Stacks', help_text='Stacks associadas')
  
  ativo = models.BooleanField(verbose_name='Está Disponível?', default=True)

  class Meta:
    verbose_name = 'Certificado'
    verbose_name_plural = 'Certificados'
    ordering = ['nome','ativo']
  
  def __str__(self):
    return f'{self.name}'
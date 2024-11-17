from django.db import models
from freitascodes.models import Stacks

class Certificados(models.Model):
  nome = models.CharField('Nome do Certificado', max_length=500)
  descricao = models.TextField('Descrição do Curso/Certificado')

  avaliable_at = models.CharField('Disponível em', help_text='Link do Certificado Online.', max_length=2000, null=True, blank=True)
  arquivo = models.FileField('Arquivo', upload_to="certificados", null=True, blank=True)
  stacks = models.ManyToManyField(Stacks, verbose_name='Stacks', help_text='Stacks associadas ao certificado.')
  
  ativo = models.BooleanField(verbose_name='Está Disponível?', default=True)

  class Meta:
    verbose_name = 'Certificado'
    verbose_name_plural = 'Certificados'
    ordering = ['nome','ativo']
  
  def __str__(self):
    return f'{self.name}'
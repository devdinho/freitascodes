from django.db import models
from freitascodes.models import Projetos

import uuid

class Imagens(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  descricao = models.TextField('Descrição da Imagem', null=True, blank=True)
  
  arquivo = models.ImageField('Imagem', upload_to=f"projetos", null=False, blank=False)

  projeto = models.ForeignKey(Projetos, verbose_name='Projeto', help_text='Projeto associado', on_delete=models.CASCADE)
  
  ordem = models.IntegerField('Ordem da imagem', default=5, help_text="Quanto maior, maior a prioridade na ordenação")

  ativo = models.BooleanField(verbose_name='Está Disponível?', default=True)

  class Meta:
    verbose_name = 'Imagem'
    verbose_name_plural = 'Imagens'
    ordering = ['projeto__name','ordem','ativo']
  
  def __str__(self):
    return f'{self.projeto.name} ({self.ordem}) - {self.descricao}'
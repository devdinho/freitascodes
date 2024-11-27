from rest_framework import viewsets
from rest_framework.response import Response

from freitascodes.models import Projetos
from freitascodes.serializers import ProjetosSerializer, ProjetosSerializerFull

class ProjetosApiView(viewsets.ModelViewSet):
  serializer_class = ProjetosSerializer

  def get_queryset(self):
    return Projetos.objects.filter(project_type=self.request.GET.get('type',1), ativo=True)
  
  def retrieve(self, request, *args, **kwargs):
      id = kwargs.get('pk')
      data = Projetos.objects.filter(id=id, ativo=True)

      projetos = ProjetosSerializerFull(data, many=True).data[0] if data else None

      return Response(projetos)
  
  def create(self, request, *args, **kwargs):
    responseData = {'mensagem':'Não permitido!'}
    return Response(responseData)
  
  def destroy(self, request, *args, **kwargs):
    responseData = {'mensagem':'Não permitido!'}
    return Response(responseData)
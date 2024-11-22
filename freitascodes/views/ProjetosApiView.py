from rest_framework import viewsets
from rest_framework.response import Response

from freitascodes.models import Projetos
from freitascodes.serializers import ProjetosSerializer

class ProjetosApiView(viewsets.ModelViewSet):
  serializer_class = ProjetosSerializer

  def get_queryset(self):
    return Projetos.objects.filter(ativo=True)
    
  def retrieve(self, request, *args, **kwargs):
    project_type = kwargs.get('pk')
    data = Projetos.objects.filter(project_type=project_type)
    messages = ProjetosSerializer(data, many=True).data[0] if data else None

    return Response(messages)
  
  def create(self, request, *args, **kwargs):
    responseData = {'mensagem':'Não permitido!'}
    return Response(responseData)
  
  def destroy(self, request, *args, **kwargs):
    responseData = {'mensagem':'Não permitido!'}
    return Response(responseData)
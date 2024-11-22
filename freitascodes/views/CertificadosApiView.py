from rest_framework import viewsets
from rest_framework.response import Response

from freitascodes.models import Certificados
from freitascodes.serializers import CertificadosSerializer

class CertificadosApiView(viewsets.ModelViewSet):
  serializer_class = CertificadosSerializer

  def get_queryset(self):
    return Certificados.objects.filter(ativo=True)
    
  def retrieve(self, request, *args, **kwargs):
    responseData = {'mensagem':'Não permitido!'}
    return Response(responseData)
  
  def create(self, request, *args, **kwargs):
    responseData = {'mensagem':'Não permitido!'}
    return Response(responseData)
  
  def destroy(self, request, *args, **kwargs):
    responseData = {'mensagem':'Não permitido!'}
    return Response(responseData)
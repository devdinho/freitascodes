from rest_framework import serializers
from django.conf import settings

from freitascodes.models import Certificados

from freitascodes.serializers import StacksSerializer

ICONS_URL = settings.ICONS_URL

class CertificadosSerializer(serializers.ModelSerializer):
  stacks = StacksSerializer(many=True)

  icons = serializers.SerializerMethodField()

  class Meta:
    model = Certificados
    fields = '__all__'
    
  def get_icons(self,obj):
    stacks = obj.stacks.all().values_list('skillicon_name', flat=True)
    icons_urls = ICONS_URL + f','.join(stacks)
    return icons_urls
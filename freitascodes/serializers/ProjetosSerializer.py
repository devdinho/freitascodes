from rest_framework import serializers
from django.conf import settings

from freitascodes.models import Projetos

from freitascodes.serializers import StacksSerializer

ICONS_URL = settings.ICONS_URL

class ProjetosSerializer(serializers.ModelSerializer):
  stacks = StacksSerializer(many=True)
  project_type_display = serializers.CharField(source='get_project_type_display')
  icons = serializers.SerializerMethodField()

  class Meta:
    model = Projetos
    fields = ['name','project_type','project_type_display','repo_name','avaliable_at','stacks','icons']
  
  def get_icons(self,obj):
    stacks = obj.stacks.all().values_list('skillicon_name', flat=True)
    icons_urls = ICONS_URL + f','.join(stacks)
    return icons_urls
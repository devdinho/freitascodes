from rest_framework import serializers

from freitascodes.models import Projetos

from freitascodes.serializers import StacksSerializer, ImagensSerializer

class ProjetosSerializerFull(serializers.ModelSerializer):
  stacks = StacksSerializer(many=True)

  imagens = serializers.SerializerMethodField()
  project_type_display = serializers.CharField(source='get_project_type_display')

  class Meta:
    model = Projetos
    fields = ['id','name','project_type_display','repo_name','avaliable_at','stacks','imagens']
  
  def get_imagens(self, obj):
    imgs = ImagensSerializer(obj.imagens_set.filter(ativo=True).order_by('-ordem'), many=True)
    return imgs.data if imgs else None

class ProjetosSerializer(serializers.ModelSerializer):
  stacks = StacksSerializer(many=True)

  imagen = serializers.SerializerMethodField()
  project_type_display = serializers.CharField(source='get_project_type_display')

  class Meta:
    model = Projetos
    fields = ['id','name','project_type_display','repo_name','avaliable_at','stacks','imagen']
  
  def get_imagen(self, obj):
    imgs = ImagensSerializer(obj.imagens_set.filter(ativo=True).order_by('-ordem'), many=True)
    return imgs.data[0] if imgs else None
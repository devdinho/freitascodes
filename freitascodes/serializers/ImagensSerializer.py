from rest_framework import serializers
from freitascodes.models import Imagens


class ImagensSerializer(serializers.ModelSerializer):
  img = serializers.SerializerMethodField()

  class Meta:
    model = Imagens
    fields = ['descricao','img','ordem','ativo']

  
  def get_img(self, obj):
    img = obj.arquivo.url
    return img
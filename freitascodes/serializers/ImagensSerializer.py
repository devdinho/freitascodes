from rest_framework import serializers

from django.contrib.sites.models import Site

from freitascodes.models import Imagens


class ImagensSerializer(serializers.ModelSerializer):
  img = serializers.SerializerMethodField()

  class Meta:
    model = Imagens
    fields = ['descricao','img','ordem',]

  
  def get_img(self, obj):
    request = self.context.get('request')
    if request:
        return request.build_absolute_uri(obj.arquivo.url)
    
    current_site = Site.objects.get(pk=1)  # Assumindo que o site com pk igual a 1 é o site atual
    return f"{current_site.domain}{obj.arquivo.url}"

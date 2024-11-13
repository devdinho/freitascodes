from rest_framework import serializers
from freitascodes.models import TipoStacks


class TipoStacksSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = TipoStacks
    fields = ['name']
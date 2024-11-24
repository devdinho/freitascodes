from rest_framework import serializers
from freitascodes.models import Stacks

# from freitascodes.serializers import TipoStacksSerializer
class StacksSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Stacks
    fields = ['name','stack_type','stack_type','skillicon_name']
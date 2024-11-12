from rest_framework import serializers
from freitascodes.models import Stacks


class StacksSerializer(serializers.ModelSerializer):
  stack_type_display = serializers.CharField(source='get_stack_type_display')
  
  class Meta:
    model = Stacks
    fields = ['name','stack_type','stack_type_display','skillicon_name']
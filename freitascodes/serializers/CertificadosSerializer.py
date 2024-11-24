from rest_framework import serializers

from freitascodes.models import Certificados

from freitascodes.serializers import StacksSerializer

class CertificadosSerializer(serializers.ModelSerializer):
  stacks = StacksSerializer(many=True)

  class Meta:
    model = Certificados
    fields = '__all__'
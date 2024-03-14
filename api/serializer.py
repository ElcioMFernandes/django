from rest_framework import serializers
from api.models import Cedente, Banco

class CedenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cedente
        fields = '__all__'

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ['nome', 'cnab']
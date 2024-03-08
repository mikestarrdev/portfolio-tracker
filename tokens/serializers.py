from rest_framework import serializers
from .models import Token

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['user', 'id', 'contract_address', 'name', 'symbol', 'decimals']

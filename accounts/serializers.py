from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user', 'id', 'address', 'token', 'amount']

    user = serializers.PrimaryKeyRelatedField(read_only=True)

from rest_framework import serializers
from .models import CryptoData

class CryptoDataSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    price = serializers.FloatField(required=True)
    one_hour = serializers.CharField(required=True)
    twentyfour_hour = serializers.CharField(required=True)
    seven_day = serializers.CharField(required=True)
    market_cap = serializers.CharField(required=True)
    volume = serializers.CharField(required=True)
    suppy = serializers.CharField(required=True)
    current_top_10 = serializers.BooleanField(required=True)

    def create(self, validated_data):
        return CryptoData.objects.create(**validated_data)
from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.FloatField()
from rest_framework import serializers
from .models import food

class foodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = food
        fields = '__all__'
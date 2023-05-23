from rest_framework import serializers
from .models import Member

class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
from .models import SmallProject, BigProject
from rest_framework import serializers

class SmallProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model=SmallProject
        fields= '__all__'

class BigProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model=BigProject
        fields= '__all__'
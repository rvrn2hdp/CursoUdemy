from rest_framework import serializers

from .models import *


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = '__all__'


class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


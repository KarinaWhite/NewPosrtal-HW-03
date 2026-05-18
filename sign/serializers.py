from rest_framework import serializers
from .models import MyModel, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel

        fields = ['id', 'title', 'content']
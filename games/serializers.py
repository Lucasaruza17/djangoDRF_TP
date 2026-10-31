from rest_framework import serializers
from .models import Game, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Game
        # 'category' es el ID para crear/editar, 'category_detail' muestra los datos anidados al leer
        fields = ['id', 'title', 'description', 'price', 'developer', 'release_date', 'category', 'category_detail']
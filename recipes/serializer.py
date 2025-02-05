from rest_framework import serializers
from recipes.models import Recipe
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe  # Specify the model
        fields = '__all__'   
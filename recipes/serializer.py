from rest_framework import serializers
from recipes.models import Recipe,Register
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe  # Specify the model
        fields = '__all__'   
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
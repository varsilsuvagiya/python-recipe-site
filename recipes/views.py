from django.shortcuts import render
from rest_framework import viewsets
from recipes.models import Recipe
from recipes.serializer import RecipeSerializer
from django.shortcuts import render, redirect
from recipes.models import Recipe
# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer
    


from django.shortcuts import render

def add_recipe(request):
  
    return render(request, 'add_recipe.html')
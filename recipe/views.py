from django.shortcuts import render,redirect,get_object_or_404
from recipes.models import Recipe,Register


def recipe_list(request):
    recipes = Recipe.objects.all()  # Fetch all recipes
    return render(request, 'recipe_list.html', {'recipes': recipes})

def add_recipe(request):
    
     if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        active = request.POST.get('active') == 'on'  # Checkbox returns 'on' if checked

        if recipe_name:  # Check if recipe_name is provided
            Recipe.objects.create(
                recipe_name=recipe_name,
                recipe_description=recipe_description,
                active=active
            )
            # return redirect('add-recipe')  # Replace with your success page or URL
        else:
            error = "Recipe name is required."

     else:
        error = None

     return render(request, 'add_recipe.html')
 
def update_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)  # Get the recipe by primary key
    if request.method == 'POST':
        recipe.recipe_name = request.POST.get('recipe_name')
        recipe.recipe_description = request.POST.get('recipe_description')
        recipe.active = request.POST.get('active') == 'on'
        
        if recipe.recipe_name:  # Ensure the recipe name is not empty
            recipe.save()
           
            return render(request, 'recipe_list.html', {'recipe': recipe})
        else:
            
            return render(request, 'recipe_list.html', {'recipe': recipe})

    return render(request, 'update_recipe.html', {'recipe': recipe})

def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk) #recipe = Recipe.objects.get(pk=pk)
    recipe.delete()
    return redirect('recipe_list')


def home_page(request):
    return render(request, 'home_page.html')

def contact_page(request):

    return render(request, 'contact_page.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        Register.objects.create(username=username, password=password, email=email, confirm_password=confirm_password)
        return redirect('register')
    return render(request, 'registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Register.objects.filter(username=username, password=password).first()
        
        if user:
            return redirect('home_page')
        else:
            error = "Invalid username or password."
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')


def logout(request):
    return redirect('login')

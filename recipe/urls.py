"""
URL configuration for recipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_page/', views.home_page, name='home_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('api/v1/', include('recipes.urls')),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('add-recipe/',views.add_recipe),
    path('update-recipe/<int:pk>/', views.update_recipe, name='update_recipe'),
    path('delete-recipe/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

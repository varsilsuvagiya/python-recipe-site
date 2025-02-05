from django.contrib import admin
from django.urls import path,include
from recipes.views import RecipeViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'recipes',RecipeViewSet)

urlpatterns = [
    path('',include(router.urls))
]
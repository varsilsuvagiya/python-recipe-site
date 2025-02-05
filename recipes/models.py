from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=2000)
    recipe_description=models.CharField(max_length=200000)
    active=models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name
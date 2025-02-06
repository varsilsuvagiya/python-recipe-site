from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name=models.CharField(max_length=2000,null=False,blank=False)
    recipe_description=models.CharField(max_length=200000)
    active=models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name
    
class Register(models.Model):
    username=models.CharField(max_length=2000,null=False,blank=False)
    email=models.CharField(max_length=2000,null=False,blank=False)
    password=models.CharField(max_length=2000,null=False,blank=False)
    confirm_password=models.CharField(max_length=2000,null=False,blank=False)
    
    def __str__(self):
        return self.name
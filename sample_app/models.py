from django.db import models 
from dj_ingredient_field.fields import IngredientField

class TestModel(models.Model):
    ingredient = IngredientField()
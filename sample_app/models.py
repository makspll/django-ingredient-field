from django.db import models
from dj_ingredient_field import IngredientField, MeasurementUnitField

# Create your models here.
class IngredientQuantity(models.Model):
    ingredient = IngredientField()
    unit = MeasurementUnitField()


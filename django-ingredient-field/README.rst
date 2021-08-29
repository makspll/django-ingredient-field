=======================
django-ingredient-field
=======================

Quick start
-----------

1. Add "dj_ingredient_field" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'dj_ingredient_field',
    ]

3. Run ``python manage.py migrate`` to create the models.

Usage
-----

Simply add the field to your model::

   from dj_ingredient_field import IngredientField

   class MyModel(models.Model):
      ingredient = IngredientField()

The value of the field is an Ingredient object::

   from dj_ingredient_field import IngredientName, Ingredient

   model.ingredient = Ingredient(IngredientName.I_ARUGULA)

All the available ingredients can be found in the ``IngredientName`` enum

Documentation 
-------------
https://django-ingredient-field.readthedocs.io/en/latest

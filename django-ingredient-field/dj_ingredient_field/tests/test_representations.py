from dj_ingredient_field import Ingredient
from django.test import TestCase

# Create your tests here.
class IngredientTests(TestCase):

    def test_same_name_equals(self):
        ing = Ingredient("a")
        ing2 = Ingredient("a")

        self.assertEqual(ing,ing2, "Ingredients with the same name are not equal")


    def test_differnet_name_not_equals(self):
        ing = Ingredient("a")
        ing2 = Ingredient("b")

        self.assertNotEqual(ing,ing2, "Ingredients with different name are equal")

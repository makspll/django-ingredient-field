from django.test import TestCase
from sample_app.models import TestModel
from dj_ingredient_field import IngredientNameChoices

# Create your tests here.
class BasicTests(TestCase):
    def test_create_test_model_model(self):
        TestModel(ingredient=IngredientNameChoices.I_ADOBO).save()

        TestModel.objects.get(pk=1)
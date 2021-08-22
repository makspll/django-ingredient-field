from dj_ingredient_field.enums import IngredientNameChoices

class Ingredient():

    def __init__(self, ingredient_name : IngredientNameChoices ) -> None:
        self.name = str(ingredient_name)
        
    
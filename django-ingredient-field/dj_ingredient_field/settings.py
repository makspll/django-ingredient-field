from django.conf import settings
from django.utils.module_loading import import_string
from .enums import IngredientName, UnitType

def import_or_default(name : str, default):
    try:
        import_string(name)
    except:
        return default


units = [
    {
        'name': 'Litre',
        'symbol': 'L',
        'unit_type': UnitType.VOLUME,
        'conversion_rate': 1e-3
    },
    {
        'name': 'Millilitre',
        'symbol': 'ml',
        'unit_type': UnitType.VOLUME,
        'conversion_rate': 1e-6
    },
    {
        'name': 'Teaspoon',
        'symbol': 'tsp',
        'unit_type': UnitType.VOLUME,
        'conversion_rate': 5e-6
    },
    {
        'name': 'Tablespoon',
        'symbol': 'tbsp',
        'unit_type': UnitType.VOLUME,
        'conversion_rate': 20e-6
    },
    {
        'name': 'Cup',
        'symbol': 'cup',
        'unit_type': UnitType.VOLUME,
        'conversion_rate': 250e-6
    },
    {
        'name': 'Pint',
        'symbol': 'pt',
        'unit_type': UnitType.VOLUME,
        'conversion_rate': 570e-6
    },
    {
        'name': 'Gallon',
        'symbol': 'gal',
        'unit_type': UnitType.VOLUME,
        'conversion_rate': 4546e-6
    },
    {
        'name': 'Gram',
        'symbol': 'g',
        'unit_type': UnitType.MASS,
        'conversion_rate': 1e-3
    },
    {
        'name': 'Milligram',
        'symbol': 'mg',
        'unit_type': UnitType.MASS,
        'conversion_rate': 1e-6
    },
]


MASS_BASE_UNIT = {
        'name': 'Killogram',
        'symbol': 'kg',
        'unit_type': UnitType.MASS,
        'conversion_rate': 1,
        'is_base_unit': True
}

VOLUME_BASE_UNIT = {
        'name': 'Cubic Metre',
        'symbol': 'm^3',
        'unit_type': UnitType.VOLUME,
        'conversion_rate': 1,
        'is_base_unit': True,
}

INGREDIENT_UNITS = import_or_default("INGREDIENT_UNITS", units) + [MASS_BASE_UNIT,VOLUME_BASE_UNIT]
INGREDIENT_UNITS = {x["name"] : x for x in INGREDIENT_UNITS}

EMPTY_UNIT = {
        'name': 'Invalid',
        'symbol': '',
        'unit_type': UnitType.VOLUME,
        'conversion_rate': -1,
}


ingredient_names = IngredientName.choices

INGREDIENT_NAMES = import_or_default("INGREDIENT_NAMES", ingredient_names)
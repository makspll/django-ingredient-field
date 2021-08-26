__version__ = "1.0.0"

from typing import Union
from .fields import IngredientField
from .enums import UnitType, IngredientName
from numbers import Number 
import copy 

class Ingredient():
    def __init__(self, name) -> None:
        self.name = str(name)

    def __str__(self):
        return str(self.name)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Ingredient) and o.name == self.name

class MeasurementUnit():
    """
        A class containing logic for cooking measurement units which have a 'base' unit.
    """
    
    def __init__(self, name : str, symbol : str, base_unit : 'MeasurementUnit', conversion_rate : Number, format_string="{symbol}", unit_type = None) -> None:
        """ 
        Creates a new MeasurementUnit instance

        :param str name: The full name of the unit, e.g.: Millilitre, Litre, Gram
        :param str symbol: The shorthand for the name of the unit, e.g.: ml, L, g
        :param base_unit: The 'base_unit', if None, then this is unit itself is a base for other units
        :type base_unit: MeasurementUnit or None
        :param Number conversion_rate: The conversion rate from the base unit (i.e. fraction of the base unit)
        :param format_string: The way to display this unit's value, can reference: name and symbol fields, defaults to "{symbol}"
        :type format_string: str, optional
        """
        if not base_unit and not unit_type:
            raise Exception("You must specify a unit_type for base units")
        
        self.name = str(name)
        self.conversion_rate = conversion_rate
        self.symbol = symbol
        self.format_string = format_string
        self.base_unit = base_unit
        self.unit_type = base_unit.unit_type if base_unit else unit_type


    def __str__(self):
        return self.format_string.format(name = self.name, symbol = self.symbol)

    def get_base_unit_amount(self, amount) -> Number:
        """ 
        Returns the equivalent base unit
        """
        return amount * (1.0/self.conversion_rate)

    def convert_to(self, amount, o : 'MeasurementUnit', density=1.0) -> Number:

        # calculate the conversion rate between mass volume units
        cross_conversion_rate = 1.0
        if o.unit_type != self.unit_type:
            if o.unit_type == UnitType.VOLUME:
                cross_conversion_rate = 1.0 / density
            elif o.unit_type == UnitType.MASS:
                cross_conversion_rate = density
        
        # convert to base units to get mass in kg and volume in m^3
        amount_base = self.get_base_unit_amount()

        return cross_conversion_rate * amount_base
    

class VolumeUnit(MeasurementUnit):
    """
        A measurement unit for volumes, the base unit is the metric Litre
    """
    base_unit = None
    
    def __init__(self, name: str, symbol: str, conversion_rate: Number, format_string="{amount} {symbol}") -> None:
        if not VolumeUnit.base_unit:
            base_unit = MeasurementUnit("Cubic Meter", 'm^3', None, 1, unit_type=UnitType.VOLUME)

        super().__init__(name, symbol, base_unit, conversion_rate, format_string=format_string)

class MassUnit(MeasurementUnit): 
    """
        A measurement unit for masses, the base unit is the metric Gram
    """
    base_unit = None

    def __init__(self, name: str, symbol: str, conversion_rate: Number, format_string="{amount} {symbol}") -> None:
            if not VolumeUnit.base_unit:
                base_unit = MeasurementUnit("Killogram", 'kg', None, 1, unit_type=UnitType.MASS)

            super().__init__(name, symbol, base_unit, conversion_rate, format_string=format_string)

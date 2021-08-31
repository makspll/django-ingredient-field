from django.contrib import admin
from sample_app.models import IngredientQuantity
from django import forms
from dj_ingredient_field.widgets import LazySelectWidget

from django.urls import reverse_lazy

# Register your models here.

class IngredientQuantityAdminForm(forms.ModelForm):
    class Meta:
        model = IngredientQuantity
        widgets = {
            'ingredient': LazySelectWidget(reverse_lazy('dj_ingredient_field:ingredients'))
        }
        fields = '__all__' # required for Django 3.x
    
@admin.register(IngredientQuantity)
class IngredientQuantityAdmin(admin.ModelAdmin):
    form = IngredientQuantityAdminForm
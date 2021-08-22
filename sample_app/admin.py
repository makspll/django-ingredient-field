from django.contrib import admin
from sample_app.models import TestModel

# Register your models here.

@admin.register(TestModel)
class AuthorAdmin(admin.ModelAdmin):
    pass
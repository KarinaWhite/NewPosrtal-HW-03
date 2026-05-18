from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, MyModel

class CategoryAdmin(TranslationAdmin):
    model = Category

class MyModelAdmin(TranslationAdmin):
    model = MyModel

admin.site.register(MyModel, MyModelAdmin)
admin.site.register(Category, CategoryAdmin)
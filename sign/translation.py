from modeltranslation.translator import register, TranslationOptions
from .models import Category, MyModel

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(MyModel)
class MyModelTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
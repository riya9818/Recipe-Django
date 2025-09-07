# forms.py
from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions','image']  
        # If your Recipe model has an 'author' field and you want the logged-in user
        # to be set automatically, change to:
        # exclude = ('author',)
        # (Adjust fields/exclude to match your actual model fields.)

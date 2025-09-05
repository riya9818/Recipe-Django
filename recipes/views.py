from django.shortcuts import render
from .models import Recipe
# Create your views here.
def RecipeListView(request):
    recipes = Recipe.objects.all()
    return render(request,'../templates/recipe_list.html',{'recipes':recipes})

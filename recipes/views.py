from django.shortcuts import render
from .models import Recipe
# Create your views here.
def RecipeListView(request):
    recipes = Recipe.objects.all()
    return render(request,'recipe_list.html',{'recipes':recipes})

def RecipeDetailView(request, pk):
    recipes= Recipe.objects.get(pk=pk)
    return render(request,'../templates/recipe_detail.html',{'recipes':recipes})
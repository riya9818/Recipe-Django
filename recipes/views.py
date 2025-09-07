from django.shortcuts import get_object_or_404, render, redirect
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import RecipeForm

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def create_recipe(request):
    if request.method == "GET":
        form = RecipeForm()
        return render(
            request,
            "create_recipe.html",
            {"form": form},
        )
    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user   # attach logged-in user
            recipe.save()
            return redirect("recipe-detail", pk=recipe.pk)
        else:
            return render(
                request,
                "create_recipe.html",
                {"form": form},
            )

def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)  # after editing go to detail page
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form, 'recipe': recipe})


def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":  # confirm deletion
        recipe.delete()
        return redirect('home')  # go back to homepage after delete
    return render(request, 'delete_recipe.html', {'recipe': recipe})


def register(request):
    if request.user.is_authenticated:
        return redirect('recipe-list')  # Redirect if already logged in

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('recipe-list')
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form})



class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('recipe-list')
        return super().dispatch(request, *args, **kwargs)
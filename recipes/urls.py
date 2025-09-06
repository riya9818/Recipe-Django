from django.urls import path
from . import views
urlpatterns=[
    path('',views.RecipeListView,name='Recipe_List'),
    path('recipe/<int:pk>/',views.RecipeDetailView,name='Recipe_Detail'),
]
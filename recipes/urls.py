from django.urls import path
from . import views
urlpatterns=[
    path('',views.RecipeListView,name='Recipe_List')
]
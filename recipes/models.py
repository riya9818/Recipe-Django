from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Recipe(models.Model):
    title= models.CharField(max_length=256)
    ingredients= models.TextField()
    instructions= models.TextField()
    published_at= models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title
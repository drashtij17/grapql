from django.db import models
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name="ingredients", on_delete=models.CASCADE
    )
class ExtendUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")
    USERNAME_FIELD = "username"   
    EMAIL_FIELD = "email"         
# Create your models here.

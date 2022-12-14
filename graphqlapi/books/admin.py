from django.contrib import admin
from .models import Book,Category,Ingredient,ExtendUser
from django.apps import apps
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(ExtendUser)

app = apps.get_app_config('graphql_auth')
for model_name, model in app.models.items():
    admin.site.register(model)
# Register your models here.

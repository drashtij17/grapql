from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from books.schema import schema  

from graphene_django.views import GraphQLView

urlpatterns = [
   path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]

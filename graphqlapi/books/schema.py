import graphene
from graphene_django import DjangoObjectType
from .models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        feilds = ('title','author')

class Query(graphene.ObjectType):
    mybook = graphene.List(BookType)
    
    def resolve_mybook(root, info, **kwargs):
        # Querying a list
        return Book.objects.all()


schema = graphene.Schema(query=Query) 
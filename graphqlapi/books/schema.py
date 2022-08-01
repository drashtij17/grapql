
from logging import NOTSET
from multiprocessing import managers
from pyexpat import model
from unicodedata import category, name
import graphene
from graphene_django import DjangoObjectType
from .models import Book,Category,Ingredient
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        feilds = ('title','author')
class CategoryType(DjangoObjectType):
    class Meta:
        model=Category
        fields = ("id", "name", "ingredients")
class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")
class Query(graphene.ObjectType):
    mybook = graphene.List(BookType)
    bookauthor = graphene.List(BookType,author=graphene.String(required=True))
    all_ingredient = graphene.List(IngredientType)
    category_name = graphene.List(CategoryType,name=graphene.String(required=True))
    def resolve_mybook(root, info, **kwargs):
        # Querying a list
        return Book.objects.all()
    
    def resolve_bookauthor(root,info,author):
        return Book.objects.filter(author=author).all()

    def resolve_all_ingredient(root,info,**kwargs):
        return Ingredient.objects.all()

    def resolve_category_name(root,info,name):
        return Category.objects.filter(name=name)
# ################################################    adding data
class IngredientMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        notes = graphene.String(required=True)
        cat=graphene.Int(required=True)
    
    ing = graphene.Field(IngredientType)
    @classmethod
    def mutate(cls,root,info, name,notes,cat):
        create_ingr = Ingredient(name=name,notes=notes,category=Category.objects.get(id=cat))
        create_ingr.save()
        return IngredientMutation(ing=create_ingr)

class Mutation(graphene.ObjectType):
    post_ingr = IngredientMutation.Field()

class UpdateIngredient(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        category = graphene.Int(required =True)
    update_ingr = graphene.Field(IngredientType)

    @classmethod
    def mutate(cls,root,info,id,category):
        geting = Ingredient.objects.get(id=id)
        print(geting.category.id)
        geting.category.id = category
        geting.save()
        return UpdateIngredient(update_ingr=geting)

class Mutation(graphene.ObjectType):
    edit_ingr = UpdateIngredient.Field()
# class CategoryMutation(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()
#         name = graphene.String(required=True)
#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls,root,info,id,name):
#         category = Category.objects.get(id=id)
#         print(category,"kkk")
#         category.name = name
#         category.save()
#         # for delete delete()
#         return CategoryMutation(category=category)
# class Mutation(graphene.ObjectType):
#     update_table = CategoryMutation.Field()
schema = graphene.Schema(query=Query,mutation=Mutation) 
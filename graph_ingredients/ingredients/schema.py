from graphene import relay, ObjectType, Schema
import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")
        
class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class IngredientInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    notes = graphene.String()
    category = graphene.Field(IngredientType)

class Query(ObjectType):
    all_categories = DjangoListField(CategoryType)
    all_ingredients = DjangoListField(IngredientType)

    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)
    
    class Arguments:
        category_data = CategoryInput(required=True)
        
    def mutate(self, info, category_data=None):
        category_instance = Category(
            name=category_data.name
        )
        category_instance.save()

        return CreateCategory(
            category=category_instance,
        )

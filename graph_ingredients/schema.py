from graphene import ObjectType, Schema
import graph_ingredients.ingredients.schema as schema

class Query(schema.Query, ObjectType):
    pass

class Mutation(ObjectType):
    create_category = schema.CreateCategory.Field()

schema = Schema(query=Query, mutation=Mutation)

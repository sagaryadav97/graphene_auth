import graphene
# from django.contrib.auth.models import Group, Permission
from graphene_django import DjangoObjectType
# from graphql_jwt.decorators import superuser_required
from .models import LoginUser


class UserType(DjangoObjectType):
    class Meta:
        model=LoginUser
        fields  = ("id","name")


class UserQuery(graphene.ObjectType):

    me = graphene.List(UserType)

    def resolve_me(root, info):
        itmes = LoginUser.objects.all()
        print(itmes)
        return LoginUser.objects.all()
            
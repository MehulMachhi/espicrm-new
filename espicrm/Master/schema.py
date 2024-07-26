# Master/schema.py

import graphene
from graphene_django import DjangoObjectType

from .models import course_levels


class CourseLevelType(DjangoObjectType):
    class Meta:
        model = course_levels
        fields = ("id" , "levels")


class Query(graphene.ObjectType):
    all_course_levels = graphene.List(CourseLevelType)

    def resolve_all_course_levels(self , info , **kwargs):
        # This will return all course level instances
        return course_levels.objects.all()


schema = graphene.Schema(query=Query)

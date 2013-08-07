from tastypie.resources import ModelResource
from api.models import *

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()

class IncomeResource(ModelResource):
    class Meta:
        queryset = Income.objects.all()

class OutcomeResource(ModelResource):
    class Meta:
        queryset = Outcome.objects.all()

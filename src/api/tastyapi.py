from tastypie.resources import ModelResource
from api.models import User, Category

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()

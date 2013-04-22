from django.http import HttpResponse
from django.core import serializers
from api.models import User, Category

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def users(request, format='json'):
    data = serializers.serialize(format, User.objects.all())
    return HttpResponse(data, content_type="application/" + format)

def categories(request, format='json'):
    data = serializers.serialize(format, Category.objects.all())
    return HttpResponse(data, content_type="application/" + format)

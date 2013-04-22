from django.http import HttpResponse
from django.core import serializers
from api.models import User, Category

import json
from tools.serializers.json import Serializer as duck_json_serializer

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def users(request, format='json'):
    data = serializers.serialize(format, User.objects.all())
    return HttpResponse(data, content_type="application/" + format)

def categories(request, format='json'):
    data = serializers.serialize(format, Category.objects.all())
    return HttpResponse(data, content_type="application/" + format)

def test(request, format='json'):
    raw_data = serializers.serialize('python', User.objects.all(), fields=('first_name', 'last_name'))
    actual_data = [d['fields'] for d in raw_data]
    return HttpResponse(json.dumps(actual_data), content_type="application/" + format)

def test2(request, format='json'):
    serializer = duck_json_serializer()
    data = serializer.serialize(User.objects.all())
    return HttpResponse(data, content_type="application/" + format)

import json

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

def users(request):
    data = [ {'first_name':'John', 'last_name': 'Lennon'}, {'first_name': 'Paul', 'last_name': 'McCartney'}]
    return HttpResponse(json.dumps(data), content_type="application/json")

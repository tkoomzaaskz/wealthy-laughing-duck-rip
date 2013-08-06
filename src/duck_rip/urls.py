from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api.tastyapi import *
from docs import views

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(CategoryResource())

urlpatterns = patterns('',
    url(r'^api/$', views.index, name='index'), # welcome page
    url(r'^api/v1/$', views.index, name='index'), # welcome page
    (r'^api/', include((v1_api.urls))), # model urls
    url(r'^docs/', include('docs.urls')), # docs pages
)

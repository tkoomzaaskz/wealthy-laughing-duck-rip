from django.conf.urls import patterns, url
from docs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^users$', views.users, name='users'),
    url(r'^categories$', views.categories, name='categories'),
    url(r'^incomes$', views.incomes, name='incomes'),
    url(r'^outcomes$', views.outcomes, name='outcomes'),
)

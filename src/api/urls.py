from django.conf.urls import patterns, url
from api import views

def get_format_urlpatterns(urlpatterns):
    """
    Supplement existing urlpatterns with corrosponding patterns that also
    include a '.format' suffix.  Retains urlpattern ordering.
    Based on https://github.com/tomchristie/django-auto-api/blob/master/autoapi/urls.py
    """
    ret = []
    for urlpattern in urlpatterns:
        # Form our complementing '.format' urlpattern
        regex = urlpattern.regex.pattern.rstrip('$') + '.(?P<format>(json|xml))'
        view = urlpattern._callback or urlpattern._callback_str
        kwargs = urlpattern.default_args
        name = urlpattern.name
        # Add in both the existing and the new urlpattern
        ret.append(urlpattern)
        ret.append(url(regex, view, kwargs, name))
    return ret

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^users/(?:(?P<id>\d+)/)?$', views.users_old, name='users'),
    url(r'^users$', views.users, name='users'),
    url(r'^categories$', views.categories, name='categories'),
    url(r'^incomes$', views.incomes, name='incomes'),
    url(r'^outcomes$', views.outcomes, name='outcomes'),
    url(r'^test$', views.test, name='test'),
    url(r'^test2$', views.test2, name='test2'),
)

urlpatterns = get_format_urlpatterns(urlpatterns)

from django.conf.urls import  url
from  main import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^data/(?P<year>[0-9]+)/$', views.WeatherYear.as_view()),
    url(r'^data/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.WeatherMonth.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
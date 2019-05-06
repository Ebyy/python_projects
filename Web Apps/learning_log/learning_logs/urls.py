from django.conf.urls import include, url
from . import views


urlpatterns = [
    #Homepage
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
]
""" Defines URL patterns for learning_logs."""
from django.conf.urls import url

from . import views


urlpatterns = [
    # Homepage
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
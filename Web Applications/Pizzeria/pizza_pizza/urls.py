from django.conf.urls import url

from . import views

urlpatterns = [
    #Homepage
    url(r'^$', views.index, name='index'),
    # Pizza types
    url(r'^pizza/$', views.pizza, name='pizza'),
    # Toppings details
    url(r'^pizza/(?P<pizza_id>\d+)/$', views.topping, name='topping'),
]



from django.conf.urls import url
from . import views

urlpatterns = [
    # Homepage
    url(r'^$', views.index, name='index'),
    # BlogPosts page
    url(r'^posts/$', views.posts, name='posts'),
    # Page with content view
    url(r'^posts/(?P<entry_id>\d+)/$', views.post, name='post'),
    # page for new post
    url(r'^new_post/$', views.new_post, name='new_post'),
    # page for new post content
    url(r'^new_entry/(?P<post_id>\d+)/$', views.new_entry, name='new_entry'),
    # page for entry edit
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]

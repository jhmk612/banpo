from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^(?P<pk>\d+)/$', views.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/post/$', views.post, name='post'),
    url(r'^(?P<person_pk>\d+)/post/(?P<post_pk>\d+)/$', views.post_detail, name='post_detail')

]
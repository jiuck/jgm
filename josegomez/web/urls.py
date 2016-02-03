
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',          views.index,    name='index'),
    url(r'^hello/$',    views.hello,    name='hello'),
    url(r'^blog/$',     views.blog,     name='blog'),
    url(r'^post/$',     views.post,     name='post'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^aboutme/$',  views.aboutme,  name='aboutme'),
]
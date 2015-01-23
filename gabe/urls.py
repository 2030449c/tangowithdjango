from django.conf.urls import patterns, url
from gabe import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='gabe'))

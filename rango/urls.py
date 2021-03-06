from django.conf.urls import patterns, url
from rango import views
from rango import searchview

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page$',
        views.add_page, name = 'add_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^search/$', searchview.search, name = 'search'),
    url(r'^goto/$', views.track_url, name = 'goto'),
    url(r'^add_profile/', views.register_profile, name = 'add_profile'),
    url(r'^profile/(?P<user_name>[\w\-]+)/$', views.profile, name = 'profile'),
    url(r'^users/', views.users, name='users'),
    )

from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
                       url(r'^login/$', views.post_login, name='login'),
                       url(r'^logout/$', views.do_logout, name='logout'),
                      )
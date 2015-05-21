from django.conf.urls import patterns, url
from status import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^me/$', views.me, name='me'),
                       url(r'^disable/(?P<rs_ip>.*)/$',
                           views.disable,
                           name='disable'),
                       url(r'^enable/(?P<rs_ip>.*)/$',
                           views.enable, name='enable'),)

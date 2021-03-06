from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'drainomote.views.index', name='index'),
                       url(r'^accounts/',
                           include('accounts.urls', namespace='accounts')),
                       url(r'^status/',
                           include('status.urls', namespace='status')),
                       url(r'^admin/', include(admin.site.urls)),)

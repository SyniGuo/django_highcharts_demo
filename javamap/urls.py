#!/usr/bin/python
#-*-coding:utf-8-*-

import views
import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'javamap.views.home', name='home'),
    # url(r'^javamap/', include('javamap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index,name='index'),
    url(r'^map/$',views.javamap,name='map'),
    url(r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.png'}),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve',{'document_root':settings.STATIC_ROOT}),
    )

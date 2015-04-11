from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^wiki/', include('wiki.urls', namespace="wiki")),
    url(r'^admin/', include(admin.site.urls)),
)

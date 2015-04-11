from django.conf.urls import patterns, url

from wiki import views

urlpatterns = patterns('',
   url(r'^$', views.Index, name='index'),
   url(r'^(?P<title>[a-zA-Z0-9_-]+)/edit/$', views.EditPage, name='editpage'),
   url(r'^(?P<title>[a-zA-Z0-9_-]+)/history/$', views.HistoryPage, name='historypage'),
   url(r'^(?P<title>[a-zA-Z0-9_-]+)/$', views.WikiPage, name='wikipage'),
)

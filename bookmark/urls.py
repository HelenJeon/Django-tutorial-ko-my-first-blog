from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

urlpatterns = [
    #url(r'^bookmark/$', ListView.as_view(model=Bookmark), name='index'),
    url(r'^$', ListView.as_view(model=Bookmark), name='index'),
    url(r'^bookmark/(?P<pk>\d+)/$', DetailView.as_view(model=Bookmark), name='detail'),
]
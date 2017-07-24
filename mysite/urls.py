# 1. 추가
from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

from mysite.views import HomeView # 1

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'), # 1
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),

    #url(r'^bookmark/$', ListView.as_view(model=Bookmark), name='index'),
    #url(r'^bookmark/(?P<pk>\d+)/$', DetailView.as_view(model=Bookmark), name='detail'),
]
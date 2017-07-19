from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),

    #url(r'^bookmark/$', ListView.as_view(model=Bookmark), name='index'),
    #url(r'^bookmark/(?P<pk>\d+)/$', DetailView.as_view(model=Bookmark), name='detail'),
]
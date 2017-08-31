# 1. 추가
# 2. 추가
#    static() 함수는 정적 파일을 처리하는 뷰를 호출하도록 그에 맞는 URL 패턴을 반환
# 3. 추가
from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

from mysite.views import HomeView # 1

from django.conf.urls.static import static # 2
from django.conf import settings # 3

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'), # 1
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^photo/', include('photo.urls', namespace='photo')), # 3

    #url(r'^bookmark/$', ListView.as_view(model=Bookmark), name='index'),
    #url(r'^bookmark/(?P<pk>\d+)/$', DetailView.as_view(model=Bookmark), name='detail'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # 3 

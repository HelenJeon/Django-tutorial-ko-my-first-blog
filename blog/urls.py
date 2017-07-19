# 1. settings.py 에서 LANGUAGE_CODE = 'ko-kr' 일 경우 동작 하지 않음
# 2. 2017/07(년도/월) 형식일 경우 month_format='%m' 추가 해야 함
from django.conf.urls import url
from blog.views import *

urlpatterns = [

	# /
	url(r'^$', PostLV.as_view(), name='index'),
	# /post/
	url(r'^post/$', PostLV.as_view(), name='post_list'),
	# /post/django-example
	url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
	# /archive
	url(r'^archive/$', PostAV.as_view(), name='post_archive'),
	# /2017/
	url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
	# /2017/nov/
	#url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'), # 1	
	# /2017/11
	url(r'^(?P<year>\d{4})/(?P<month>[0-9]+)/$', PostMAV.as_view(month_format='%m'), name='post_month_archive'), # 2
	# /2017/nov/10/
	#url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),
	# /2017/07/19
	url(r'^(?P<year>\d{4})/(?P<month>[0-9]+)/(?P<day>[0-9]{1,2})/$', PostDAV.as_view(month_format='%m'), name='post_day_archive'),
	# /today/
	url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),	
	
] 

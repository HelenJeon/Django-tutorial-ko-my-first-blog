# 1. ListView 제네릭 뷰를 상속받아 PostLV 클래스형 뷰 정의
# 2. 대상 테이블은 Post
# 3. 템플릿 파일에 넘겨주는 객체 리스트에 대한 컨텍스트 변수명은 posts
#    별도로 posts로 지정해도 디폴트 컨텍스트 변수명인 object_list 역시 사용 가능
# 4. 변경날짜가 최근인 포스트 먼저 출력
# 5. make_object_list = True 이면 해당 년도에 해당하는 객체 리스트를 만들어서 템플릿에 넘겨줌
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post

# ListView
class PostLV(ListView) : # 1
	model = Post # 2
	template_name = 'blog/post_all.html'
	context_object_name = 'posts' # 3
	paginate_by = 2

# DetailView
class PostDV(DetailView) :
	model = Post
	
# ArchiveIndexView
class PostAV(ArchiveIndexView) :
	model = Post
	date_field = 'modify_date' # 4

class PostYAV(YearArchiveView) :
	model = Post
	date_field = 'modify_date'
	make_object_list = True # 5

class PostMAV(MonthArchiveView) :
	model = Post
	date_field = 'modify_date'

class PostDAV(DayArchiveView) :
	model = Post
	date_field = 'modify_date'

class PostTAV(TodayArchiveView) :
	model = Post
	date_field = 'modify_date'

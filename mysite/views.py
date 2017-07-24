# 1. TemplateView 제네릭 뷰를 상속
# 2.템플릿 파일 위치 디렉토리는 settings.py 의 TEMPLATES_DIRS 항목으로 지정
from django.views.generic.base import TemplateView

class HomeView(TemplateView) : # 1
    template_name = 'home.html' #2
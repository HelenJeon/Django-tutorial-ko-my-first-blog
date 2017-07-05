from django.shortcuts import render
from bookmark.models import Bookmark # 테이블 조회를 위해 import

# ListView
# ListView 제네릭 뷰를 상속
# 명시적으로 지정하지 않아도 장고에서 지정해 주는 속성
#   1) 컨텍스트 변수로 object_list를 사용
#   2) 템플릿 파일을 모델명소문자_list.html 이름으로 지정
class BookmarkLV(ListView):
    model = Bookmark

# DetailView
# DetailView 제네릭 뷰를 상속
# 명시적으로 지정하지 않아도 장고에서 지정해 주는 속성
#   1) 컨텍스트 변수로 object를 사용
#   2) 템플릿 파일을 모델명소문자_detail.html 이름으로 지정
class BookmarkDV(DetailView):
    model = Bookmark    

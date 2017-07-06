from django.shortcuts import render
from bookmark.models import Bookmark # 테이블 조회를 위해 모델 클래스를 import

# ListView
# ListView 제네릭 뷰를 상속
#   cf. 제네릭 뷰: 공통적 기능 추상화하여 장고에서 기본적으로 제공해주는 클래스형 뷰
#   cf. 클래스형 뷰: 클래스로 작성되어 있는 뷰 객체, 객체 지향 기술 가능하여 코드의 재사용성과 생산성을 높여줌
# 명시적으로 지정하지 않아도 장고에서 지정해 주는 속성
#   1) 컨텍스트 변수로 object_list를 사용
#   2) 템플릿 파일을 templates\모델명\모델명소문자_list.html 이름으로 지정
#   3) 적용안될 경우 서버 재시작
class BookmarkLV(ListView):
    model = Bookmark

# DetailView
# DetailView 제네릭 뷰를 상속
# 명시적으로 지정하지 않아도 장고에서 지정해 주는 속성
#   1) 컨텍스트 변수로 object를 사용
#   2) 템플릿 파일을 templates\모델명\모델명소문자_detail.html 이름으로 지정
class BookmarkDV(DetailView):
    model = Bookmark    

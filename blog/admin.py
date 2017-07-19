# 1. Post 클래스가 Admin 사이트에서 보여지는 모습 정의
# 2. slug 필드는 title 필드를 사용해 미리 채워지도록 함
# 3. admin.site.register() 함수를 사용해 Post와 PostAdmin 클래스를 Admin 사이트에 등록
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin): # 1
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)} # 2

admin.site.register(Post, PostAdmin) # 3

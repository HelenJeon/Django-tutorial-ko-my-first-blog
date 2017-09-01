# 1. pyhton2, python3문자열 처리 방식 다름
#    호환성 유지하기 위해 임포트
# 2. URL 패턴 생성
# 3. 슬러그: 페이지나 포스트를 설명하는 핵심 단어 집합, 특수문자제외하고 제목공백"-"로 연결해 생성 
#    SlugField 디폴트 길이는 50, 인덱스가 디폴트로 생성
# 4. auto_now_add: 객체가 생성될 때 시각
# 5. auto_now: 객체가 데이터베이스에 저장될 때 시각
# 6. 테이블 단수 명칭 post, 복수 명칭 posts, modify_date 내림차순 정렬

from __future__ import unicode_literals # 1
from django.utils.encoding import python_2_unicode_compatible # 1

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse    # 2

@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='title alias') # 3
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='description text')
    text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    #modify_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField('Create Date', auto_now_add=True) # 4
    modify_date = models.DateTimeField('Modify Date', auto_now=True)      # 5 
    published_date = models.DateTimeField(blank=True, null=True)
    
    class Meta: # 6
        verbose_name = 'post'           
        verbose_name_plural = 'posts'   
        db_table = 'blog_post'
        ordering = ('-modify_date',)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
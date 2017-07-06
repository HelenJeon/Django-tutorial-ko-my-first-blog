# 1) pyhton2, python3문자열 처리 방식 다름
#    호환성 유지하기 위해 임포트
# 2) URL 패턴 생성
# 3) auto_now_add: 객체가 생성될 때 시각
# 4) auto_now: 객체가 데이터베이스에 저장될 때 시각
# 5) 슬러그: 페이지나 포스트를 설명하는 핵심 단어 집합, 특수문자제외하고 제목공백"-"로 연결해 생성 
#    SlugField 디폴트 길이는 50, 인덱스가 디폴트로 생성
from __future__ import unicode_literals # 1)
from django.utils.encoding import python_2_unicode_compatible # 1)

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse    # 2)

@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='title alias') # 5)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='description text')
    text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    #modify_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField('Create Date', auto_now_add=True) # 3)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)      # 4) 
    published_date = models.DateTimeField(blank=True, null=True)

        class Meta:
                verbose_name = 'post'
                verbose_name_plural = 'posts'
                db_table = 'my_post'
                ordering = ('-modify_date',)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
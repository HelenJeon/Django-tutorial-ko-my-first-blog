from __future__ import unicode_literals # python 2.x 지원
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self): # 객체를 문자열로 표현할 때 사용
        return self.title



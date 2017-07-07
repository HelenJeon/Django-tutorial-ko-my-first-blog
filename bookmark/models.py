# 1.
# 2. 객체를 문자열로 표현할 때 사용, title 반환

from __future__ import unicode_literals # 1
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self): # 2
        #return self.title
        return "%s %s" %(self.title, self.url)



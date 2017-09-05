# 1. pyhton2, python3문자열 처리 방식 다름
#    호환성 유지하기 위해 임포트
# 2. URL 패턴 생성
# 3. 커스텀 필드, 커스텀 필드는 fields.py에 정의
#    cf) 커스텀 필드: django에서 제공하지 않는, 서드 파티에서 스스로 정의한 필드
# 4. django에서 객체를 문자열로 표현하기 위해서 다음과 같이 지원
#    @python_2_unicode_compatible 데코레이터를 정의
#    파이썬3 문법인 __str__() 메소드만을 사용(파이썬2에서는 django에서 알아서 변환)
# 5. 본 사진이 소속된 앨범 객체를 가리키는 reference

from __future__ import unicode_literals # 1
from django.utils.encoding import python_2_unicode_compatible # 1

from django.db import models

from django.core.urlresolvers import reverse # 2

from photo.fields import ThumbnailImageField # 3

@python_2_unicode_compatible # 4
class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

@python_2_unicode_compatible
class Photo(models.Model):
    album = models.ForeignKey(Album) # 5
    title = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='media/photo/%Y/%m')
    description = models.TextField('Photo Description', blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', arg=(self.id,))




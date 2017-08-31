# 1. django의 기본 필드 import
# 2. 설치한 파이썬의 이미지 처리 라이브러리
# 3. 썸네일 이미지 파일명
#    ex) a.jpg -> a.thumb.jpg
#    - 이미지 확장자가 jpeg/jpg가 아니면 jpg로 변경
# 4. ImageFieldFile을 상속, 파일 시스템에 직접 파일을 쓰고 지우는 작업
# 5. 파일 경로와 url
# 6. 파일 저장, 생성
# 7. 백그라운드+이미지 thumbnail 생성
# 8. 파일 삭제시에 원본/썸네일 모두 삭제
# 9. ImageField 상속, 이 클래스가 장고 모델 정의에 사용하는 필드 역할
# 10. ThumbnailImageField 같은 새로운 클래스를 정의할 때에는 그에 상응하는 File 처리 클래스를 attr_class 속성에 지정하는 것이 필수
#     ThumbnailImageField 상응하는 File 클래스로 #4. ThumbnailImageFieldFile 을 지정
# 11. 부모 ImageField 클래스의 생성자를 호출하여 관련 속성들 초기화

from django.db.models.fields.files import ImageField, ImageFieldFile # 1
from PIL import Image, ImageOps # 2
import os

def _add_thumb(s): # 3
    parts = s.split(".")
    parts.insert(-1, "thumb")
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)

class ThumbnailImageFieldFile(ImageFieldFile): # 4
    def _get_thumb_path(self): # 5
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self): # 5
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True): # 6
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)

        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS)
        #background = Image.new('RGBA', size, (255,255,255,0))
        background = Image.new('RGB', img.size, (255,255,255,0))
        background.paste(img, ( int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2) )) # 7
        background.save(self.thumb_path, 'JPEG')

    def delete(self, save=True): # 8
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)
    
class ThumbnailImageField(ImageField): # 9
    attr_class = ThumbnailImageFieldFile # 10

    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs): # 11
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)


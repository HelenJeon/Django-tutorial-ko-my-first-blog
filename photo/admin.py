# 1. 앨범 객체를 보여주는 형식
#    StackedInline: 세로 나열, TabularInline: 행 나열
# 2. 앨범 객체를 보여줄때 PhotoInline 클래스에서 정의한 사항을 같이 보여줌

from django.contrib import admin

from photo.models import Album, Photo

class PhotoInline(admin.StackedInline): # 1
    model = Photo
    extra = 2

class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline] # 2
    list_display = ('name', 'description')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)

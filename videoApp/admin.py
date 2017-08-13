from django.contrib import admin
from models import Album,Video
# Register your models here.
class AlbumAdmin(admin.ModelAdmin):

    list_display = ['album_title' , 'group']
    search_fields = ['album_title', 'group']
    class Meta:
        model = Album

admin.site.register(Album, AlbumAdmin)

class VideoAdmin(admin.ModelAdmin):

    list_display = ['video_title', 'album']
    search_fields = ['video_title']

    class Meta:
        model = Video

admin.site.register(Video, VideoAdmin)
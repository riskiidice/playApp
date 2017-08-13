from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
    group = models.CharField(max_length=10)
    album_title = models.CharField(max_length=255)
    album_description = models.CharField(max_length=255)
    album_logo = models.FileField(upload_to='album/%Y/%m/%d')

    def __str__(self):
        return self.album_title


class Video(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='video/%Y/%m/%d')
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.video_title+' '+self.album_title
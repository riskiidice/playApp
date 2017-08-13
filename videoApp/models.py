from __future__ import unicode_literals
from django.contrib.auth.models import Group
from django.db import models

# Create your models here.
class Album(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=255)
    album_description = models.CharField(max_length=255)
    album_logo = models.FileField(upload_to='album/%Y/%m/%d')

    def __unicode__(self):
        return unicode(self.album_title)

    def __str__(self):
        return self.album_title


class Video(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='video/%Y/%m/%d')
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return unicode(self.video_title)

    def __str__(self):
        return self.video_title+' '+self.album.album_title
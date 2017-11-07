from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    title = models.CharField('Заголовок', max_length=500)
    short = models.CharField('Краткое описание', max_length=500, blank=True)
    content = RichTextUploadingField('Контент')
    posted_datetime = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def __str__(self):
        return "%s - %s - %s" % (self.title, self.posted_datetime, self.active)

    class Meta:
        ordering = ['-posted_datetime']


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=2000)
    post = models.ForeignKey(Post, related_name='comments')

    def __str__(self):
        return "%s - %s" % (self.created_at, self.post)

    class Meta:
        ordering = ['created_at']

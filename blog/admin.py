from django.contrib import admin
from django.contrib.admin import DateFieldListFilter, ModelAdmin

from blog.models import Post, Tag, Comment


class Postdmin(ModelAdmin):
    list_filter = (
        ('posted_datetime', DateFieldListFilter), 'tags', 'active'
    )


admin.site.register(Post, Postdmin)
admin.site.register(Comment)
admin.site.register(Tag)

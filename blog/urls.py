from django.conf.urls import url
from django.contrib import admin

from blog.views import IndexPageView, CommentApiView, PostView, TagListView

urlpatterns = [
    url(r'^$', IndexPageView.as_view()),
    url(r'^post/(?P<pk>[\d]+)$', PostView.as_view(), name='post-detail'),
    url(r'^tags$', TagListView.as_view(), name='tag-list'),
    url(r'^api/comments/$', CommentApiView.as_view(), name='comment-api')
]

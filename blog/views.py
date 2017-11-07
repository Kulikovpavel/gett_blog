from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from blog.models import Post, Comment, Tag


class IndexPageView(View):
    def get(self, request):
        tag = request.GET.get('tag', None)
        posts = Post.objects.filter(active=True)
        if tag:
            posts = posts.filter(tags=tag)
        return render(request, 'index.html', {'posts': posts})


class CommentApiView(View):
    def post(self, request):
        post = Post.objects.get(id=request.POST['post_id'])
        Comment.objects.create(post=post, text=request.POST['text'])
        return HttpResponse()


class PostView(DetailView):
    model = Post
    template_name = 'post-detail.html'


class TagListView(ListView):
    model = Tag
    template_name = 'tag-list.html'

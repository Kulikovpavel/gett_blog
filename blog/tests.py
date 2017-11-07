from django.test import TestCase, Client
from django.urls import reverse_lazy

from blog.models import Tag, Post, Comment


class ModelsTestCase(TestCase):
    def test_create(self):
        p = Post.objects.create(title='title1', content='content1')
        t = Tag.objects.create(title="tag1")
        p.tags.add(t)

        Comment.objects.create(text='sss', post=p)


class IndexTestCase(TestCase):
    def setUp(self):
        t1 = Tag.objects.create(title="tag1")
        t2 = Tag.objects.create(title="tag2")

        p1 = Post.objects.create(title='title1', content='content1')
        p1.tags.add(t1, t2)

        p2 = Post.objects.create(title='title2', content='content2')
        p2.tags.add(t1)

        p3 = Post.objects.create(title='title3', content='content3')

    def test_posts(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 3)
        self.assertContains(response, 'title1')
        self.assertContains(response, '/?tag=')


class CommentAPITestCase(TestCase):
    def setUp(self):
        p1 = Post.objects.create(title='title1', content='content1')
        self.post_id = p1.id

    def test_comment(self):
        c = Client()
        response = c.post(reverse_lazy('comment-api'), {'post_id': self.post_id, 'text': 'comment1'})
        self.assertEqual(response.status_code, 200)

        comment = Comment.objects.get(post=self.post_id)
        self.assertEqual(comment.text, 'comment1')


class PostTestCase(TestCase):
    def setUp(self):
        p = Post.objects.create(title='title1', content='content1')
        t = Tag.objects.create(title="tag1")
        p.tags.add(t)
        self.post_id = p.id

    def test_view(self):
        c = Client()
        response = c.get(reverse_lazy('post-detail', kwargs={'pk': self.post_id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'title1')
        self.assertContains(response, 'content1')
        self.assertContains(response, '/?tag')

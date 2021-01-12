from django.test import TestCase
from blog.models import BlogPost, BlogImage, BlogComment
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class TestBlogModel(TestCase):
    def test_blog_post(self):
        blog = BlogPost(title='blog_title', category='category')
        self.assertEqual(str(blog), 'blog_title, category')


class TestBlogImageModel(TestCase):

    def test_blog_image(self):
        user_1 = User(username='test_user_1')
        user_1.save()
        blog = BlogPost(title='blog_title', category='category', author=user_1)
        blog.save()
        blog_image = BlogImage(article_id=blog)
        blog_image.image = SimpleUploadedFile(name='test_image.jpg',
                                              content=b'',
                                              content_type='image/jpeg')
        self.assertEqual(str(blog_image),
                         'test_image.jpg, blog_title, category')

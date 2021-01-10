from django.test import TestCase
from blog.models import BlogPost, BlogImage, BlogComment
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class TestBlogFeed(TestCase):
    """
    Tests for views renders templates in blog app
    """

    def setUp(self):

        # Create author
        author = User.objects.create_superuser('author',
                                               'author@test.com',
                                               'authorpassword')

        # Create user for comment
        user_comment = User.objects.create_user('comment_user',
                                                'comment@test.com',
                                                'commentpassword')

        self.test_post = BlogPost(title='test_title',
                                  slug='test_title',
                                  author=author,
                                  category='test_category',
                                  content='blog_content',
                                  status=1)
        self.test_post.save()

        self.blog_image = BlogImage(article_id=self.test_post)
        self.blog_image.image = SimpleUploadedFile(name='test_image.jpg',
                                                   content=b'',
                                                   content_type='image/jpeg')
        self.blog_image.save()
        self.test_blogcomment = BlogComment(article_id=self.test_post,
                                            user_id=user_comment,
                                            comment_title='test_comment_title')
        self.test_blogcomment.save()

    def test_blog_feed(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_category_view(self):

        response = self.client.get('/blog/category_view/{0}/'
                                   .format(self.test_post.category))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'blog/post_category_view.html')

    def test_post_view(self):
        response = self.client.get('/blog/blog_detail/{0}/'
                                   .format(self.test_post.slug))
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_add_blog(self):
        self.client.login(username='author', password='authorpassword')
        response = self.client.get('/blog/add/')
        self.assertTemplateUsed(response, 'blog/add_blog.html')
        self.client.logout()
        self.client.login(username='comment_user', password='commentpassword')
        response = self.client.get('/blog/add/')
        self.assertRedirects(response, '/',
                             status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

    def test_edit_blog(self):
        self.client.login(username='author', password='authorpassword')
        response = self.client.get('/blog/edit/{0}/'
                                   .format(self.test_post.pk))
        self.assertTemplateUsed(response, 'blog/edit_blog.html')

    def test_delete_blog(self):
        self.client.login(username='author', password='authorpassword')
        response = self.client.get('/blog/delete/{0}/'
                                   .format(self.test_post.pk),
                                   follow=True)
        self.assertRedirects(response, '/blog/',
                             status_code=302, target_status_code=200,
                             fetch_redirect_response=True)

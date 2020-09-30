from django.db import models
from django.contrib.auth.models import User
 
STATUS = (
   (0, "Draft"),
   (1, "Publish")
)

class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    category = models.CharField(max_length=254, null=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True,  verbose_name='post_created_date')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    image = models.ImageField(null=True, blank=True)
    article_id = models.ForeignKey('BlogPost', null=True,
                                  blank=True, on_delete=models.SET_NULL, verbose_name='image_article_id')


class BlogComments(models.Model):
    article_id = models.ForeignKey('BlogPost', null=True, related_name="comments",
                                    blank=True, on_delete=models.SET_NULL)
    comment_name = models.CharField(max_length=50)
    blog_comment = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='comment_created_date')

    def __str__(self):
        return '%s - %s' % (self.article_id.title, self.comment_name)
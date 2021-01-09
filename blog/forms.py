from .models import BlogPost, BlogImage, BlogComment
from django import forms


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('slug', 'created_on', 'status', 'updated_on', 'author')


class BlogImageForm(forms.ModelForm):
    class Meta:
        model = BlogImage
        fields = ('image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('comment_title', 'blog_comment')

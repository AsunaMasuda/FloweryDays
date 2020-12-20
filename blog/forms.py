from .models import BlogComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('comment_title', 'blog_comment')

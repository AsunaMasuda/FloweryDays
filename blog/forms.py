from .models import BlogComments
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComments
        fields = ('comment_title', 'blog_comment')

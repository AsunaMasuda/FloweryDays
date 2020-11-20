from .models import BlogComments
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComments
        fields = ('comment_name', 'blog_comment')

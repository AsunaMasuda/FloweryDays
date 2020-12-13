from django import template
from blog.models import BlogImage

register = template.Library()


@register.filter(name='in_image')
def in_image(blog_image, pk):
    return blog_image.filter(article_id=pk)

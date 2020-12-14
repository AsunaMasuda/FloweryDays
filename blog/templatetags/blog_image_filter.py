from django import template

register = template.Library()


@register.filter(name='in_image')
def in_image(blog_image, pk):
    """A template tag to render post image in the specified layout"""

    return blog_image.filter(article_id=pk)

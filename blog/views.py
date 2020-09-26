from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import BlogPost, BlogImage, BlogComments

def blog_feed(request):
    #order by newest first for blog_post
    blog_post = BlogPost.objects.all().order_by('-created_on')
    blog_image = BlogImage.objects.all()
    blog_comments = BlogComments.objects.all()

    # Pagination
    paginator = Paginator(blog_post, 5)
    page = request.GET.get('page')

    try:
        blog_post = paginator.page(page)
    except PageNotAnInteger:
        blog_post = paginator.page(1)
    except EmptyPage:
        blog_post = paginator.page(paginator.num_pages)

    context = {
        'blog_post': blog_post,
        'blog_image': blog_image,
        'blog_comments': blog_comments,
    }

    return render(request, 'blog/blog.html', context)
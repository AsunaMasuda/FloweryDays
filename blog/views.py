from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import BlogPost, BlogImage, BlogComments


def blog_feed(request):
    #order by newest first for blog_post
    blog_post = BlogPost.objects.all().order_by('-created_on')
    blog_image = BlogImage.objects.all()

    category_dict = dict()
    for key in blog_post:
        if key.category in category_dict.keys():
            category_dict[key.category] += 1
        else:
            category_dict[key.category] = 1

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
        'category_dict': category_dict,
    }

    return render(request, 'blog/blog.html', context)


def category_view(request, category):
    selected_blog = BlogPost.objects.all().filter(category__icontains=category)
    blog_image = BlogImage.objects.all()
    blog_post = BlogPost.objects.all()

    category_dict = dict()
    for key in blog_post:
        if key.category in category_dict.keys():
            category_dict[key.category] += 1
        else:
            category_dict[key.category] = 1

    context = {
        'selected_blog': selected_blog,
        'blog_image': blog_image,
        'category_dict': category_dict,
        'category': category,
    }

    return render(request, 'blog/post_category_view.html', context)


def post_view(request, slug):
    blog_post = BlogPost.objects.get(slug=slug)
    blog_image = BlogImage.objects.get(article_id=blog_post.id)
    
    context = {
        'blog_post': blog_post,
        'blog_image': blog_image,
    }
    
    return render(request, 'blog/post_detail.html', context)
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .models import BlogPost, BlogImage, BlogComment
from .forms import BlogForm, BlogImageForm, CommentForm


def blog_feed(request):
    """A view to render blog posts ordered by newest first with paginations"""

    blog_post = BlogPost.objects.all().order_by('-created_on')
    blog_image = BlogImage.objects.all()
    total_post_number = blog_post.count()

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
        'total_post_number': total_post_number,
    }

    return render(request, 'blog/blog.html', context)


def category_view(request, category):
    """A view to display blog posts with a selected category"""

    blog_post = BlogPost.objects.all().order_by('-created_on')
    selected_blog = blog_post.filter(category__icontains=category)
    total_post_number = blog_post.count()
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
        'total_post_number': total_post_number,
    }

    return render(request, 'blog/post_category_view.html', context)


def post_view(request, slug):
    """A view to render the article and the comments and handle posting
    new comments"""

    blog_post = get_object_or_404(BlogPost, slug=slug)
    blog_image = BlogImage.objects.get(article_id=blog_post.id)
    new_comment = None
    template = 'blog/post_detail.html'

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article_id = blog_post
            # Save the comment to the database
            new_comment.save()
            comment_form = CommentForm()
            messages.success(request, 'Successfully posted your comment.')
    else:
        comment_form = CommentForm()

    if 'last_item' in request.session:
        del request.session['last_item']

    context = {
        'blog_post': blog_post,
        'blog_image': blog_image,
        'comment_form': comment_form,
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_pk):
    """Delete a comment posted by the user"""

    comment = get_object_or_404(BlogComment, pk=comment_pk)
    slug = comment.article_id.slug
    comment.delete()

    if 'last_item' in request.session:
        del request.session['last_item']

    messages.success(request, 'Successfully deleted your comment.')
    return redirect(post_view, slug)


@login_required
def add_blog(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners have access to the area.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        blog_form = BlogForm(request.POST)
        blog_image_form = BlogImageForm(request.POST, request.FILES)
        if blog_form.is_valid() and blog_image_form.is_valid():
            # Create Blog object but don't save to database yet
            new_blog = blog_form.save(commit=False)
            new_blog_image = blog_image_form.save(commit=False)
            # Assign the auther to the new blog and save it
            new_blog.author = request.user
            new_blog.save()
            # Assign the blog to the new image and save it
            new_blog_image.article_id_id = new_blog.pk
            new_blog_image.save()
            messages.success(request, 'Successfully posted your blog.')
        else:
            messages.error(
                request, 'Failed to add the blog. Please ensure the form is valid.')

    else:
        blog_form = BlogForm()
        blog_image_form = BlogImageForm()

    if 'last_item' in request.session:
        del request.session['last_item']

    template = 'blog/add_blog.html'
    context = {
        'blog_form': blog_form,
        'blog_image_form': blog_image_form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_pk):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only site owner have access to the area.')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(BlogPost, pk=blog_pk)
    blog_image = get_object_or_404(BlogImage, article_id=blog_pk)

    if request.method == 'POST':
        blog_form = BlogForm(request.POST, instance=blog_post)
        blog_image_form = BlogImageForm(request.POST, request.FILES, instance=blog_image)

        if blog_form.is_valid() and blog_image_form.is_valid():
            # Create Blog object but don't save to database yet
            new_blog = blog_form.save(commit=False)
            new_blog_image = blog_image_form.save(commit=False)
            # Assign the auther to the new blog and save it
            new_blog.author = request.user
            new_blog.save()
            # Assign the blog to the new image and save it
            new_blog_image.article_id_id = new_blog.pk
            new_blog_image.save()
            messages.success(request, f'You updated {blog_post.title}!')

            if 'last_item' in request.session:
                del request.session['last_item']

            return redirect(reverse('post_view', args=[blog_post.slug]))
        else:
            messages.error(
                request, 'Failed to update blog. Please ensure the form is valid.')

    else:
        blog_form = BlogForm(instance=blog_post)
        blog_image_form = BlogImageForm(request.POST, request.FILES, instance=blog_image)
        messages.info(
            request, f'You are editing a product details: {blog_post.title}')

    template = 'blog/edit_blog.html'
    context = {
        'blog_form': blog_form,
        'blog_image_form': blog_image_form,
        'blog_post': blog_post,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_pk):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only site owner have access to the area.')
        return redirect(reverse('home'))

    blog = get_object_or_404(BlogPost, pk=blog_pk)
    blog.delete()
    messages.success(request,
                     f'You deleted blog title: {blog.title} from the database.')

    if 'last_item' in request.session:
        del request.session['last_item']

    return redirect(reverse('blog'))

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from .models import Group
POSTS_NUMBER: int = 10  # Количество постов, отображаемых на странице


def index(request):
    posts = Post.objects.select_related('group').all()
    paginator = Paginator(posts, POSTS_NUMBER)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = group.posts.all()
    paginator = Paginator(posts, POSTS_NUMBER)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)

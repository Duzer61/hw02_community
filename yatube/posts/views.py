from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Group
POSTS_NUMBER: int = 10  # Количество постов, отображаемых на странице


def index(request):
    posts = (Post.objects.select_related('group').order_by('-pub_date')
             [:POSTS_NUMBER])
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = (Post.objects.select_related('group').filter(group=group)
             .order_by('-pub_date')[:POSTS_NUMBER])
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)

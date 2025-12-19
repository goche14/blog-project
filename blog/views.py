from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = (
        Post.objects
        .select_related('author', 'author__profile')
        .prefetch_related('tags')
        .order_by('-created_at')
    )

    return render(request, 'posts/post_list.html', {
        'posts': posts
    })


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects
        .select_related('author', 'author__profile')
        .prefetch_related(
            'comments__author',
            'tags'
        ),
        id=post_id
    )

    return render(request, 'posts/post_detail.html', {
        'post': post
    })

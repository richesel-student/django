# from django.shortcuts import get_object_or_404, render

# from .models import Post
# from django.http import Http404

# # Create your views here.

# def post_detail(reqest, id):
#     post = get_object_or_404(
#         Post,
#         id=id,
#         status=Post.Status.PUBLISHED
#     )
    
# def post_list(reqest):
#     posts = Post.published.all()
#     return render(
#         reqest,
#         'blog/post/list.html',
#         {'posts' : posts}
#     )

# def post_detail(request, id):
#     try:
#         post = Post.published.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404("No Post found.")
#     return render(
#         request,
#         'blog/post/detail.html',
#         {'post' : post}
#     )
from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
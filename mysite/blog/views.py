from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import Http404

# Create your views here.

def post_detail(reqest, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    
def post_list(reqest):
    post = Post.published.all()
    return render(
        reqest,
        'blog/post/list.html',
        {'post' : post}
    )

def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    return render(
        request,
        'blog/post/detail.html',
        {'post' : post}
    )
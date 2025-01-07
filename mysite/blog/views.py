from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView


from .forms import EmailPostForm
from .models import Post
from django.http import Http404

# Create your views here.


def post_share(request, post_id):
# Извлечь пост по идентификатору id 
    post = get_object_or_404(
    Post,
    id=post_id,
    status=Post.Status.PUBLISHED
    )
    if request.method == 'POST':
# Форма была передана на обработку 
        form = EmailPostForm(request.POST)
        if form.is_valid():
# Поля формы успешно прошли валидацию
           cd = form.cleaned_data
# ... отправить электронное письмо
    else:
        form = EmailPostForm()
    return render( 
        request,
        'blog/post/share.html', {
        'post': post,
        'form': form 
        }
    )


def post_list(reqest):
    post_list = Post.published.all()
    # Построение разбивки с 3 постами на странице
    paginator = Paginator(post_list, 3)
    page_number = reqest.GET.get('page', 1)
    
    try:
        posts = paginator.page(page_number)

    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        reqest,
        'blog/post/list.html',
        {'posts' : posts}
    )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post' : post}
    )

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html' 

# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id)
#     return render(request, 'blog/post_detail.html',{'post' : post})
    


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
# from django.shortcuts import get_object_or_404, render

# from .models import Post


# def post_list(request):
#     posts = Post.published.all()
#     return render(
#         request,
#         'blog/post/list.html',
#         {'posts': posts}
#     )


# def post_detail(request, id):
#     post = get_object_or_404(
#         Post,
#         id=id,
#         status=Post.Status.PUBLISHED
#     )
#     return render(
#         request,
#         'blog/post/detail.html',
#         {'post': post}
#     )
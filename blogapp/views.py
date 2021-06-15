from django.core import paginator
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post

def index(request):
    template = 'index.html'
    post = Post.objects.all()
    paginator = Paginator(post,3)

    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)

    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {
        'page_obt':page,
        'posts': post}

    return render(request, template_name=template,context=context)


def single_post(request,number,title):
    template = 'single_post.html'
    post = get_object_or_404(Post,slug = title, id = number)
    context = {
        'post':post
    }
    return render(request,template_name=template,context=context)

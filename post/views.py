from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, Http404

from .forms import PostForm, CommentForm
from .models import Post, Comment

# Create your views here.


def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'postlar': posts})


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    if not request.user.is_authenticated:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Kayıt başarılı bir şekilde oluşturuldu')
        # İlgili postun detay sayfasına yönlendirme yapıyoruz
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


def post_update(request, slug):
    if not request.user.is_authenticated:
        raise Http404

    post = get_object_or_404(Post, slug=slug)
    # GET ile gelindiğinde sadece instance=post bilgileri ile form nesnesi oluşturulur
    # POST ile gelindiğinde istek ile gelen form bilgilerindeki parametreler ile form nesnesi oluşturulur, instance
    # verildği için de form bunu changed data ile tutarak güncelleme yapacağını anlar. Instance verilmez ise create olur
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save()
        messages.success(request, 'Kayıt başarılı bir şekilde güncellendi')
        # İlgili postun detay sayfasına yönlendirme yapıyoruz
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


def post_delete(request, slug):
    if not request.user.is_authenticated:
        raise Http404

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('post_app:index')
    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)

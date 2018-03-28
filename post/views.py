from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect

from .forms import PostForm
from .models import Post


# Create your views here.


def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'postlar': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save()
        messages.success(request, 'Kayıt başarılı bir şekilde oluşturuldu')
        # İlgili postun detay sayfasına yönlendirme yapıyoruz
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    # GET ile gelindiğinde sadece instance=post bilgileri ile form nesnesi oluşturulur
    # POST ile gelindiğinde istek ile gelen form bilgilerindeki parametreler ile form nesnesi oluşturulur, instance
    # verildği için de form bunu changed data ile tutarak güncelleme yapacağını anlar. Instance verilmez ise create olur
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save()
        messages.success(request, 'Kayıt başarılı bir şekilde güncellendi')
        # İlgili postun detay sayfasına yönlendirme yapıyoruz
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('post_app:index')
    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)

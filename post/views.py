from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.core.paginator import Paginator

from .forms import PostForm, CommentForm
from .models import Post
from django.db.models import Q

# Create your views here.


# Arama yapılmışsa sonucu bul ve döndür
def get_search(req):
    query = req.GET.get('q')
    if query:
        p_list = Post.objects.all()
        return p_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query)
        ).distinct()
    else:
        return None


def post_index(request):

    if get_search(request):
        post_list = get_search(request)
    else:
        post_list = Post.objects.all()

    paginator = Paginator(post_list, 2)  # Show 2 post per page

    page = request.GET.get('sayfa')
    posts = paginator.get_page(page)

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

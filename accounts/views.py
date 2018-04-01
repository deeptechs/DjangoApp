from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm


# Create your views here.


def login_view(request):
    # Login olunmuş ise ana sayfaya
    if request.user.is_authenticated:
        return redirect('home:home')

    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        # authenticate yanlış loginde hata fırlatır, form bunu yakalar ve clean metodu ile validasyona verir.
        user = authenticate(username=username, password=password)
        # Hata alınmaz ise kullanıcıyı login et ve anasayfaya yönlen
        login(request, user)
        return redirect('home:home')

    context = {
        'form': form,
        'title': 'Giriş'
    }

    return render(request, 'accounts/form.html', context)


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        # Form user modelden türediği için save metodu user objesini dönüyor
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = True Yönetici sayfasına giriş hakkı
        # user.is_superuser = True Yönetici sayfasında değişiklik hakkı
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('home:home')

    context = {
        'form': form,
        'title': 'Üye Ol'
    }

    return render(request, 'accounts/form.html', context)


def logout_view(request):
    logout(request)
    return redirect('home:home')
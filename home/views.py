from django.shortcuts import render

# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        context = {
            'isim': request.user.get_username(),
        }
    else:
        context = {
            'isim': 'Misafir',
        }
    return render(request, 'home.html', context)

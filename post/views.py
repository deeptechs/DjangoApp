from django.shortcuts import render, HttpResponse

# Create your views here.


def post_index(request):
    return HttpResponse('<b>Index Sayfası<b>')


def post_detail(request):
    return HttpResponse('<b>Detail Sayfası<b>')


def post_create(request):
    return HttpResponse('<b>Create Sayfası<b>')


def post_update(request):
    return HttpResponse('<b>Update Sayfası<b>')


def post_delete(request):
    return HttpResponse('<b>Delete Sayfası<b>')


from django.urls import path

from post.views import *

# Url name ler karışmasın diye, app_name tanımlanıyor
app_name = 'post_app'

urlpatterns = [

    path('', post_index),
    path('index/', post_index, name='index'),
    path('create/', post_create, name='create'),
    path('<str:slug>/', post_detail, name='detail'),
    path('<str:slug>/update/', post_update, name='update'),
    path('<str:slug>/delete/', post_delete, name='delete'),

]

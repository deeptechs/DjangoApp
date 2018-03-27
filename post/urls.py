from django.urls import path
from post.views import *

# Url name ler karışmasın diye, app_name tanımlanıyor
app_name ='post_app'

urlpatterns = [

    path('', post_index),
    path('index/', post_index, name='index'),
    path('<int:id>/', post_detail, name='detail'),
    path('create/', post_create, name='create'),
    path('<int:id>/update/', post_update, name='update'),
    path('<int:id>/delete/', post_delete, name='delete'),

]





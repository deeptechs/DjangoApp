from django.urls import path
from post.views import *


urlpatterns = [

    path('', post_index),
    path('index/', post_index),
    path('detail/', post_detail),
    path('create/', post_create),
    path('update/', post_update),
    path('delete/', post_delete),

]





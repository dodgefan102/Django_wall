from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('post',views.postblog),
    path('comment', views.comment),
    path('comdelete',views.comdelete),
    path('postdelete', views.postdelete)
]
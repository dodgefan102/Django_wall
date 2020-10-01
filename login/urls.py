from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('register', views.reg),
    path('success',views.success),
    path('login',views.log),
    path('logout',views.out)
]
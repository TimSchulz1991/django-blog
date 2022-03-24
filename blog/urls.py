from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post_detail"),
    # first slug is a path converter
    # https://docs.djangoproject.com/en/3.2/topics/http/urls/#how-django-processes-a-request
    # second slug comes from PostDetail class from views.py
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),
]
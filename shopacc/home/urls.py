from turtle import home
from django.urls import path
from .views import index, home
urlpatterns = [
    path("", index.as_view(), name='index'),
    path("trang-chu/", home.as_view(), name='home'),
]
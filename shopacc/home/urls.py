from turtle import home
from django.urls import path
from .views import index, home, detail
urlpatterns = [
    path("", index.as_view(), name='index'),
    path("trang-chu/", home.as_view(), name='home'),
    path("mua-tai-khoan/<slug:slug>", detail.as_view(), name='detail'),
]
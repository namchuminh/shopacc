from turtle import home
from django.urls import path
from .views import index, home, detail, pay, category, contact
urlpatterns = [
    path("", index.as_view(), name='index'),
    path("trang-chu/", home.as_view(), name='home'),
    path("mua-tai-khoan/<slug:slug>", detail.as_view(), name='detail'),
    path("thanh-toan/<slug:slug>", pay.as_view(), name='pay'),
    path("chuyen-muc/<slug:slug>", category.as_view(), name='category'),
    path("lien-he/", contact.as_view(), name='contact'),
]
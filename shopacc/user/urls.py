from django.urls import path
from .views import Userlogin, Userlogout, Userchangeinfo, Usersigup, Ajax, Cartuser
urlpatterns = [
    path("dang-nhap/", Userlogin.as_view(), name='user-login'),
    path("dang-ky/", Usersigup.as_view(), name='user-sigup'),
    path("dang-xuat/", Userlogout.as_view(), name='user-logout'),
    path("tai-khoan/", Userchangeinfo.as_view(), name='change-info'),
    path("ajax/", Ajax.as_view(), name='ajax'),
    path("gio-hang/", Cartuser.as_view(), name='user-cart')
]
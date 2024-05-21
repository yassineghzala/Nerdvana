from xml.etree.ElementInclude import include
from django.urls import path

from User.views import getUserByEmail, userGP, userGPD # type: ignore






urlpatterns = [
    path("users",userGP, name="users_crud"),
    path("users/<int:pk>",userGPD, name="users_crud"),
    path("users/<str:email>",getUserByEmail, name="users_byemail_crud"),
]
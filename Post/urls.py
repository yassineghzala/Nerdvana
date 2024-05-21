from xml.etree.ElementInclude import include
from django.urls import path

from Post import views
from Post.views import postGP, postGPD


urlpatterns = [
    path("posts",postGP, name="posts_crud"),
    path("posts/<int:pk>",postGPD, name="posts_crud"),
]
from xml.etree.ElementInclude import include
from django.urls import path

from Comment.views import  commentGP, commentGPD # type: ignore






urlpatterns = [
    path("comments",commentGP, name="comments_crud"),
    path("comments/<int:pk>",commentGPD, name="comments_crud"),
]
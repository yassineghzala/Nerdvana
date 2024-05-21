from xml.etree.ElementInclude import include
from django.urls import path

from Message.views import  messageGP, messageGPD






urlpatterns = [
    path("messages",messageGP, name="messages_crud"),
    path("messages/<int:pk>",messageGPD, name="messages_crud"),
]
from xml.etree.ElementInclude import include
from django.urls import path

from Command.views import commandsGP, commandsGPD


urlpatterns = [
    path("commands",commandsGP, name="commandss_crud"),
    path("commands/<int:pk>",commandsGPD, name="commands_crud"),
]
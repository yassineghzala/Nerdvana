from xml.etree.ElementInclude import include
from django.urls import path

from Poster import views
from Poster.views import PostersByAlbumView, posterGP, posterGPD, PostersByAlbumView, PostersByArtistView


urlpatterns = [
    path("posters",posterGP, name="posters_crud"),
    path("posters/<int:pk>",posterGPD, name="posters_crud"),
    path("posters/postersByArtist/<str:artist>",PostersByArtistView.as_view(),name="postersByArtist_crud"),
    path("posters/postersByAlbum/<str:album>",PostersByAlbumView.as_view(),name="postersByAlbum_crud"),
]
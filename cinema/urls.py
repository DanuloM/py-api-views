from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet, GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    CinemaHallDetailViewSet,
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("genre/", GenreList.as_view(), name="genre-list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actor/", ActorList.as_view(), name="actor-list"),
    path("actor/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path(
        "cinemahall/",
        CinemaHallViewSet.as_view(action={"get": "list", "post": "create"}),
        name="cinemahall-list"
    ),
    path(
        "cinemahall/<int:pk>",
        CinemaHallDetailViewSet.as_view(
            action={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="cinemahall-detail",
    ),
]

app_name = "cinema"

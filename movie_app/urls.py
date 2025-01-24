# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("director/", views.DirectorListAPIView.as_view(), name="director-list"),
    path(
        "director/<int:pk>",
        views.DirectroDetailAPIView.as_view(),
        name="director-detail",
    ),
    path("movie/", views.MovieDetailAPIView.as_view(), name="movie-list"),
    path("movie/<int:pk>", views.MovieDetailAPIView.as_view(), name="movie-detail"),
    path("rewiew/", views.RewiewDetailAPIView.as_view(), name="rewiew-list"),
    path(
        "rewiew/<int:pk>",
        views.RewiewDetailAPIView.as_view(),
        name="rewiew-detail",
    ),
]

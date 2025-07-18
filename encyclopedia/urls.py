"""URL configuration for encyclopedia app."""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_title>", views.entry, name="entry"),
    path("new_entry", views.new_entry, name="new_entry"),
    path("wiki/<str:entry_title>/edit", views.edit, name="edit"),
    path("random_entry", views.random_entry, name="random_entry"),
    path("search", views.search, name="search"),
]

HANDLER404 = "encyclopedia.views.error_404_view"

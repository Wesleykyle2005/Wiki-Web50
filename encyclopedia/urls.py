from django.urls import path
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("new_entry", views.new_entry, name="new_entry"),
    path("wiki/<str:entry>/edit", views.edit, name="edit"),
    path("random_entry", views.random_entry, name="random_entry"),
    path("search", views.search, name="search")
]


handler404 = 'encyclopedia.views.error_404_view'
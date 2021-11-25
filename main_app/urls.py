from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("about/", views.about, name="about"),
  path("musicians/", views.musicians_index, name="musicians_index"),
  path("musicians/<int:musician_id>/", views.musicians_detail, name="musicians_detail"),
  path("musicians/create/", views.MusicianCreate.as_view(), name="musicians_create"),
  path("musicians/<int:pk>/update/", views.MusicianUpdate.as_view(), name="musicians_update"),
  path("musicians/<int:pk>/delete/", views.MusicianDelete.as_view(), name="musicians_delete"),
  path("musicians/<int:musician_id>/add_song/", views.add_song, name="add_song"),
]
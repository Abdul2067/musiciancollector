from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("about/", views.about, name="about"),
  path("musicians/", views.musicians_index, name="musicians_index"),
  path("musicians/<int:musician_id>/", views.musicians_detail, name="musicians_detail"),
]
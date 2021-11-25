from django.db import models
from django.urls import reverse

# Create your models here.

class Musician(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("musicians_detail", kwargs={"musician_id": self.id})

class Song(models.Model):
  song_name = models.CharField(max_length=50)
  album = models.CharField(max_length=50)

  musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

  def __str__(self):
    return self.song_name
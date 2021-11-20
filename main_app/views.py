from django.shortcuts import render


class Musician:
  def __init__ (self, name, genre, description, age):
    self.name = name
    self.genre = genre
    self.description = description
    self.age = age

musicians = [
  Musician("Drake", "Hip-Hop", "Awesome Artist", "30"),
  Musician("Drake", "Hip-Hop", "Awesome Artist", "30"),
  Musician("Drake", "Hip-Hop", "Awesome Artist", "30"),
  Musician("Drake", "Hip-Hop", "Awesome Artist", "30")
]

# Create your views here.

def home(request):
  return render(request, "home.html")

def about(request):
  return render(request, "about.html")

def musicians_index(request):
  return render(request, "musicians/index.html", { "musicians" : musicians})
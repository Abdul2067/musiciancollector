from django.shortcuts import render
from .models import Musician

# Create your views here.

def home(request):
  return render(request, "home.html")

def about(request):
  return render(request, "about.html")

def musicians_index(request):
  musicians = Musician.objects.all()
  return render(request, "musicians/index.html", { "musicians" : musicians})

def musicians_detail(request, musician_id):
  musician = Musician.objects.get(id=musician_id)
  return render(request, "musicians/detail.html", { "musician" : musician})
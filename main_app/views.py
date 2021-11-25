from django.db.models import fields
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Musician
from .forms import SongForm

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
  song_form = SongForm()
  return render(request, "musicians/detail.html", { "musician" : musician, "song_form" : song_form})

class MusicianCreate(CreateView):
  model = Musician
  fields = "__all__"

class MusicianUpdate(UpdateView):
  model = Musician
  fields = ["genre", "description", "age"]

class MusicianDelete(DeleteView):
  model = Musician
  success_url = "/musicians/"

def add_song(request, musician_id):
  form =  SongForm(request.POST)
  if form.is_valid():
    new_song = form.save(commit=False)
    new_song.musician_id = musician_id
    new_song.save()
  return redirect("musicians_detail", musician_id=musician_id)
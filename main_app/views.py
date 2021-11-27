from django import contrib
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Musician, Streaming
from .forms import SongForm
from main_app import models

# Create your views here.

class Home(LoginView):
  template_name = "home.html"

def about(request):
  return render(request, "about.html")

@login_required
def musicians_index(request):
  musicians = Musician.objects.filter(user=request.user)
  return render(request, "musicians/index.html", { "musicians" : musicians})

@login_required
def musicians_detail(request, musician_id):
  musician = Musician.objects.get(id=musician_id)
  streams_musician_doesnt_have = Streaming.objects.exclude(id__in = musician.streams.all().values_list("id"))
  song_form = SongForm()
  return render(request, "musicians/detail.html", { "musician" : musician, "song_form" : song_form, "streams" : streams_musician_doesnt_have})

class MusicianCreate(LoginRequiredMixin ,CreateView):
  model = Musician
  fields = ["name", "genre", "description", "age"]

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class MusicianUpdate(LoginRequiredMixin ,UpdateView):
  model = Musician
  fields = ["genre", "description", "age"]

class MusicianDelete(LoginRequiredMixin ,DeleteView):
  model = Musician
  success_url = "/musicians/"

@login_required
def add_song(request, musician_id):
  form =  SongForm(request.POST)
  if form.is_valid():
    new_song = form.save(commit=False)
    new_song.musician_id = musician_id
    new_song.save()
  return redirect("musicians_detail", musician_id=musician_id)

class StreamingCreate(LoginRequiredMixin ,CreateView):
  model = Streaming
  fields = "__all__"

class StreamingList(LoginRequiredMixin ,ListView):
  model = Streaming

class StreamingDetail(LoginRequiredMixin ,DetailView):
  model = Streaming

class StreamingUpdate(LoginRequiredMixin ,UpdateView):
  model = Streaming
  fields = "__all__"

class StreamingDelete(LoginRequiredMixin ,DeleteView):
  model = Streaming
  success_url = "/streams/"

@login_required
def assoc_streaming(request, musician_id, streaming_id):
  Musician.objects.get(id=musician_id).streams.add(streaming_id)
  return redirect("musicians_detail", musician_id=musician_id)

def signup(request):
  error_message = ""
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("musicians_index")
    else:
      error_message = "Invalid sign up, please try again"
  form = UserCreationForm()
  context = {"form": form, "error_message": error_message}
  return render(request, "signup.html", context)

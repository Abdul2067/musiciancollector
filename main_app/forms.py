from django.forms import ModelForm, fields
from .models import Song

class SongForm(ModelForm):
  class Meta:
    model = Song
    fields = ["song_name", "album"]
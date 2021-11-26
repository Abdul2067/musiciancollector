from django.contrib import admin

from .models import Musician, Song, Streaming

# Register your models here.

admin.site.register(Musician)
admin.site.register(Song)
admin.site.register(Streaming)
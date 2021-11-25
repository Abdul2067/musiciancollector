from django.contrib import admin

from .models import Musician, Song

# Register your models here.

admin.site.register(Musician)
admin.site.register(Song)
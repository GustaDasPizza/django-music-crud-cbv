# catalog/models.py
from django.db import models
from django.urls import reverse

class Song(models.Model):
    title = models.CharField("Título", max_length=200)
    artist = models.CharField("Artista", max_length=200)
    album = models.CharField("Álbum", max_length=200, blank=True, null=True)
    genre = models.CharField("Gênero", max_length=100)
    release_date = models.DateField("Data de Lançamento(AAAA-MM-DD)", blank=True, null=True)

    class Meta:
        ordering = ['artist', 'title'] 

    def __str__(self):
        return f"{self.title} - {self.artist}"

    def get_absolute_url(self):
        return reverse('song-detail', kwargs={'pk': self.pk})
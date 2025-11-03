# catalog/views.py
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Song

class SongListView(ListView):
    model = Song
    template_name = 'catalogo/listar.html'
    context_object_name = 'songs'

class SongDetailView(DetailView):
    model = Song
    template_name = 'catalogo/detalhe.html'
    context_object_name = 'song'

class SongCreateView(CreateView):
    model = Song
    template_name = 'catalogo/form.html'
    fields = ['title', 'artist', 'album', 'genre', 'release_date'] 

class SongUpdateView(UpdateView):
    model = Song
    template_name = 'catalogo/form.html'    
    fields = ['title', 'artist', 'album', 'genre', 'release_date']
 
class SongDeleteView(DeleteView):
    model = Song
    template_name = 'catalogo/confirm_delete.html' 
    context_object_name = 'song'
    success_url = reverse_lazy('song-list')
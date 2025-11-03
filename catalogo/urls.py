# catalog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SongListView.as_view(), name='song-list'),
    
    path('song/<int:pk>/', views.SongDetailView.as_view(), name='song-detail'),
    
    path('song/create/', views.SongCreateView.as_view(), name='song-create'),
    
    path('song/<int:pk>/update/', views.SongUpdateView.as_view(), name='song-update'),
    
    path('song/<int:pk>/delete/', views.SongDeleteView.as_view(), name='song-delete'),
]
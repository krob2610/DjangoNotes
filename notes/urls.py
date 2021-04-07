#from django.conf.urls import url
from django.urls import path

from .views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView


urlpatterns = [
    path('', NoteListView.as_view(),name='note-list'),
    path('<int:pk>/', NoteDetailView.as_view(),name='note-detail'),
    path('create', NoteCreateView.as_view(), name='note-create'),
    path('<int:pk>/update', NoteUpdateView.as_view(),name='note-update'),
    path('<int:pk>/delete', NoteDeleteView.as_view(),name='note-delete')
]

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .forms import NoteForm
from .models import Note
# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "index.html", {})



class NoteListView(ListView):
    model = Note
class NoteDetailView(DetailView):
    model = Note

class NoteCreateView(LoginRequiredMixin,CreateView):
    template_name = 'notes/note_create.html'
    form_class = NoteForm
    queryset = Note.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.create_by = self.request.user  #<-----------nie działa
        return super(NoteCreateView, self).form_valid(form)

class NoteUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'notes/note_create.html'
    form_class = NoteForm
    queryset = Note.objects.all()

    def test_func(self):
        return self.request.user == self.get_object().created_by
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, DeleteView):  #UserPassesTestMixin
    model = Note
    template_name = 'notes/note_delete.html'
    #success_url = reverse_lazy('notes:note-list') #jeśli zrobimy funkcje get_succes_url to uzyjemy reverse (w klasach lazy w funkcjach zwykly reverse)

    def get_success_url(self):
        return reverse('notes:note-list')
    def test_func(self):
        return self.request.is_superuser or self.request.user == self.object.created_by

#class NoteDetailView(ListView):
 #   form_class = NoteForm
  #  template_name = 'list.html'
   # queryset = Note.objects.all()

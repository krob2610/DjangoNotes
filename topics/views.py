from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from notes.models import Note
from .models import Topic


class TopicListView(ListView):
    model = Topic


class TopicDetailView(DetailView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(topic=self.get_object().pk)
        return context


class TopicCreate(LoginRequiredMixin, CreateView):
    template_name = 'topics/topic_create.html'
    model = Topic
    fields = ['title', 'parent']
    success_url = reverse_lazy('topic-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TopicCreate, self).form_valid(form)



class TopicUpdate(UserPassesTestMixin, UpdateView):
    template_name = 'topics/topic_create.html'
    model = Topic
    fields = ['title', 'parent']
    success_url = reverse_lazy('topic-list')
    def test_func(self):
        return self.request.user == self.get_object().created_by

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TopicDelete(LoginRequiredMixin, DeleteView):
    template_name = 'topics/topic_delete.html'
    model = Topic
    success_url = reverse_lazy('topic-list')

    def test_func(self):
        return self.request.is_superuser or self.request.user == self.object.created_by

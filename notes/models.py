from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from topics.models import Topic
class Note(TimeStampedModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,null = True )
    title = models.CharField(max_length=256)
    body = models.TextField()
    created_by = models.ForeignKey(User,default = 'current_user', on_delete=models.CASCADE) #from django.http import HttpRequest <-----------curent user
    def get_absolute_url(self):
        return reverse("note-detail", kwargs={"pk":self.pk})
    def __str__(self):
        return self.title

from django.contrib import admin

# Register your models here
from .models import Topic
from django_mptt_admin.admin import DjangoMpttAdmin
admin.site.register(Topic)
class TopicAdmin(DjangoMpttAdmin):
    list_display = ['title', 'is_public']
    list_editable = ['is_public']

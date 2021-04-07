from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

# drzewiasta zależność - Home > Products > Food > Meat > Spam > Spammy McDelicious

class Topic(MPTTModel, TitleSlugDescriptionModel, TimeStampedModel): #TimeStampedModel - created and modified fields.   TitleSlugDescriptionModel  provides title and description fields
    parent = TreeForeignKey('self', on_delete = models.CASCADE, null=True, blank=True, related_name='children', db_index=True)
    is_public = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class MPTTMeta:
        order_insertion_by = ['title']  #lass adds some tweaks to django-mptt - in this case, just order_insertion_by. This indicates the natural ordering of the data in the tree

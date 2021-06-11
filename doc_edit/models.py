from django.db import models
from django.conf import settings
import datetime
from froala_editor.fields import FroalaField


class documentRoom(models.Model):
    name        = models.CharField(max_length=100)
    date_create = models.DateTimeField()
    users       = models.ManyToManyField(settings.AUTH_USER_MODEL, help_text="users who are in the room")

    def __str__(self):
        return self.name


class document(models.Model):
    title       = models.CharField(max_length=150)
    content     = FroalaField()
    docRoom     = models.ForeignKey(documentRoom, on_delete=models.CASCADE)
    date        = datetime.datetime.now()

    def __str__(self):
        return self.title


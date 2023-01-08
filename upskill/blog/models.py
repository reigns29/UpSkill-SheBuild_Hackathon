from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

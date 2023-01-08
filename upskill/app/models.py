from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Email(models.Model):
    email = models.EmailField(max_length = 122)
        
    def __str__(self):
        return self.email



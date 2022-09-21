import email
from email import message
from unicodedata import name
from venv import create
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name

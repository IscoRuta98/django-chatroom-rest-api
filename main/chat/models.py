from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class ChatMessage(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    message_content = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.sender} to {self.receiver} at {self.timestamp}: {self.message_content}"

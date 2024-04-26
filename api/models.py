#models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True)
    completed=models.BooleanField(default=False,null=True, blank=True)

    class Meta:
        ordering = ["due_date"]
    def __str__(self):
        return self.title
    
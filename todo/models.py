from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    """Defines a todo item.
    Owner: whose item this is
    description: what needs to be done
    done: task was completed?
    updated: when was the last time the owner wrote here?
    """
    owner = models.ForeignKey(User)
    description = models.CharField(max_length=30)
    done = models.BooleanField()
    updated = models.DateTimeField(auto_now_add=True)

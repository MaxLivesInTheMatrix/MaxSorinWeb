from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Most of this is for my own learning. I don't think ill deploy any of this
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If a user is deleted, delete the users posts too
    
    def __str__(self):
        return self.title
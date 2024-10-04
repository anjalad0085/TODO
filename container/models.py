from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200, null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    progress = models.CharField(max_length=50, default='In Progress') 
    def __str__(self):
        return self.user.username
    

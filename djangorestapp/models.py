from django.db import models
from datetime import datetime


class Blog(models.Model):
    title = models.CharField(max_length=100)
    #images
    image = models.ImageField(upload_to="images/")
    #videos
    video = models.FileField(upload_to="media/", null=True)
    description = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

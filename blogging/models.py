from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        set publish date to the date when post's published status is
        switched to True, reset the date if post is unpublished
        """
        if self.published_date is None:
            self.published_date = datetime.now()
        super().save(*args, **kwargs)
    

class Category(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name="categories")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

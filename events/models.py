from django.db import models
from django.contrib.auth.models import User
from datetime import date
from taggit.managers import TaggableManager


class Event(models.Model):
    """
    Event model, related to 'owner', i.e. a User instance.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    event_date = models.DateField(blank=False)
    tags = TaggableManager(blank=True)
    image = models.ImageField(
        upload_to="images/", default="../eventsdefault_n2yze8", blank=False
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"

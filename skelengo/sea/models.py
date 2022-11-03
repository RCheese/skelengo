from uuid import uuid4

from django.db import models
from taggit.managers import TaggableManager


class Ship(models.Model):
    class Meta:
        verbose_name = "Ship"
        verbose_name_plural = "Ships"
        ordering = ("-created",)

    id = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title

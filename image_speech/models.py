import uuid

from django.db import models


class Image(models.Model):
    uuid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4(),
    )
    image_url = models.URLField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )


class Speech(models.Model):
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
    )
    uuid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4(),
    )
    transcript = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

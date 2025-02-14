from django.db import models

from src.common.models import TimeStampedModel


class Note(TimeStampedModel):
    content = models.TextField(max_length=128)
    card = models.ForeignKey(
        "cards.Card",
        related_name="notes",
        on_delete=models.CASCADE,
    )

from django.db import models
from src.common.models import TimeStampedModel


class Deck(TimeStampedModel):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True, max_length=255)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        to="users.User", on_delete=models.CASCADE, related_name="decks"
    )

    class Meta:
        verbose_name = "deck"
        verbose_name_plural = "decks"

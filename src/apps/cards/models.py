from django.db import models

from src.common.models import TimeStampedModel


class Card(TimeStampedModel):
    question = models.TextField(max_length=325)
    answer = models.TextField(max_length=325)
    user = models.ForeignKey(
        "users.User", related_name="cards", on_delete=models.CASCADE
    )
    deck = models.ForeignKey(
        "decks.Deck", related_name="cards", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "card"
        verbose_name_plural = "cards"


class CardState(models.Model):
    answered = models.BooleanField(default=False)
    card = models.OneToOneField(
        Card,
        related_name="card_state",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "card_state"

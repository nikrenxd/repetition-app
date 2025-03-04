import pytest

from src.apps.cards.models import Card
from src.apps.cards.services import CardService


@pytest.mark.django_db
def test_create_card_state():
    card = Card.objects.get(pk=2)
    CardService.create_card_state(card)

    assert card.card_state.answered is False


@pytest.mark.django_db
def test_update_card_state():
    data = {"answered": True}
    card = Card.objects.get(pk=1)
    CardService.update_card_state(card, data, 1)

    assert card.card_state.answered is True

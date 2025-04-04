import pytest

from src.apps.decks.services import DeckServices


@pytest.mark.django_db
def test_deck_change_completed(deck):
    result = DeckServices.deck_change_completed(deck, True)
    assert result is True


@pytest.mark.django_db
def test_deck_completed(deck):
    result = DeckServices.deck_completed(deck)

    assert result is None


@pytest.mark.django_db
def test_deck_update_decks_statistic(deck_qs):
    deck_stats = DeckServices.deck_update_decks_statistic(qs=deck_qs, user_id=2)

    assert deck_stats["total_decks"] > 0

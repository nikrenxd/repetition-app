import logging
from django.db import DatabaseError
from django.db.models import QuerySet, Count, Q


from src.apps.decks.models import Deck
from src.apps.users.models import UserStatistic


logger = logging.getLogger(__name__)


class DeckServices:
    @staticmethod
    def change_deck_state(deck: Deck, value: bool) -> bool:
        deck.completed = value
        deck.save()

        return value

    @staticmethod
    def complete_deck(deck: Deck) -> bool | None:
        try:
            not_answered_cards_in_deck = deck.cards.filter(
                card_state__answered=False
            ).count()

            if not_answered_cards_in_deck == 0:
                DeckServices.change_deck_state(deck, True)
                return True
            elif not_answered_cards_in_deck != 0 and deck.completed is True:
                DeckServices.change_deck_state(deck, False)
        except DatabaseError as e:
            logger.error(f"Error when updating deck completion state {e}")

    @staticmethod
    def update_deck_statistic(
        qs: QuerySet[Deck], user_id: int
    ) -> dict[str, int] | None:
        try:
            decks_stats = qs.aggregate(
                total_decks=Count("id"),
                completed_decks=Count("id", filter=Q(completed=True)),
            )
            UserStatistic.objects.filter(user_id=user_id).update(**decks_stats)
            return decks_stats
        except DatabaseError as e:
            logger.error(f"Error when updating deck statistic {e}")

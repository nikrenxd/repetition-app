import logging

from src.apps.cards.models import Card, CardState


logger = logging.getLogger(__name__)


class CardService:
    @staticmethod
    def create_card_state(card_instance: Card):
        CardState.objects.create(card=card_instance)

    @staticmethod
    def update_card_state(card: Card, data: dict, card_id: int):
        try:
            card_state = CardState.objects.get(card=card)
            card_state.answered = data.get("answered")
            card_state.save()

            logger.info("Card state updated")
        except CardState.DoesNotExist:
            logger.error(f"Error when updating card state for {card_id}")

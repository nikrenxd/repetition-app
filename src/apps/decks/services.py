from src.apps.decks.models import Deck


class DeckServices:
    @staticmethod
    def deck_change_completed(deck: Deck, value: bool) -> bool:
        deck.completed = value
        deck.save()

        return value

    @staticmethod
    def deck_completed(deck: Deck) -> bool | None:
        not_answered_cards_in_deck = deck.cards.filter(
            card_state__answered=False
        ).count()

        if not_answered_cards_in_deck == 0:
            DeckServices.deck_change_completed(deck, True)
            return True
        elif not_answered_cards_in_deck != 0 and deck.completed is True:
            DeckServices.deck_change_completed(deck, False)

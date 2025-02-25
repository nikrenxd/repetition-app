from src.apps.decks.models import Deck
from src.common.permissions import CurrentUserOwnObjectPermission


class CardCurrentUserOwnDeckPermission(CurrentUserOwnObjectPermission):
    obj_name_in_request = "deck"
    model = Deck

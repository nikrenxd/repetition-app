from src.apps.cards.models import Card
from src.common.permissions import CurrentUserOwnObjectPermission


class NoteCurrentUserOwnCardPermission(CurrentUserOwnObjectPermission):
    obj_name_in_request = "card"
    model = Card

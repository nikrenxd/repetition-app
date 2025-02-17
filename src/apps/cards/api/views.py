from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from src.apps.cards.api.serializers import CardSerializer, CardCreateSerializer
from src.apps.cards.models import Card
from src.apps.decks.models import Deck
from src.common.mixins import OwnObjectMixin


class CardViewSet(ModelViewSet, OwnObjectMixin):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs: QuerySet = super().get_queryset()

        return qs.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "create" or self.action == "partial_update":
            return CardCreateSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        self.own_object("deck", Deck)
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        self.own_object("deck", Deck)
        super().perform_update(serializer)

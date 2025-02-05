from django.db.models import QuerySet
from rest_framework import viewsets, permissions

from src.apps.decks.api.serializers import DeckSerializer, DeckCreateSerializer, DeckRetrieveSerializer
from src.apps.decks.models import Deck


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        qs: QuerySet = super().get_queryset()

        return qs.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "create" or self.action == "partial_update":
            return DeckCreateSerializer
        if self.action == "retrieve":
            return DeckRetrieveSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

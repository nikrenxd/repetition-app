from django.db.models import QuerySet, Count
from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

from src.apps.decks.api.serializers import (
    DeckSerializer,
    DeckCreateUpdateSerializer,
    DeckRetrieveSerializer,
)
from src.apps.decks.models import Deck


class DeckFilter(filters.FilterSet):
    completed = filters.BooleanFilter()

    class Meta:
        model = Deck
        fields = {
            "name": ["icontains"],
        }


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filterset_class = DeckFilter
    ordering_fields = ["name", "created_at"]
    http_method_names = ["get", "post", "delete", "patch"]

    def get_queryset(self):
        qs: QuerySet = super().get_queryset().filter(user=self.request.user)

        if self.action == "list":
            return qs.annotate(cards_num=Count("cards"))
        if self.action == "retrieve":
            return qs.prefetch_related("cards__card_state")

        return qs

    def get_serializer_class(self):
        if self.action == "create" or self.action == "partial_update":
            return DeckCreateUpdateSerializer
        if self.action == "retrieve":
            return DeckRetrieveSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

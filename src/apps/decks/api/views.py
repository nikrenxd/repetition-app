import logging

from django.db.models import QuerySet, Count, Prefetch
from django.http import HttpResponseRedirect
from rest_framework import viewsets, permissions, status
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse

from src.apps.cards.models import Card
from src.apps.decks.api.serializers import (
    DeckSerializer,
    DeckCreateUpdateSerializer,
    DeckRetrieveSerializer,
    DeckEndSerializer,
)
from src.apps.decks.models import Deck
from src.apps.decks.services import DeckServices

logger = logging.getLogger(__name__)


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
        qs: QuerySet[Deck] = super().get_queryset().filter(user=self.request.user)
        fetch_cards_qs: QuerySet[Card] = Card.objects.select_related(
            "card_state"
        ).prefetch_related("notes")

        if self.action == "list":
            return qs.annotate(cards_num=Count("cards"))
        if self.action == "retrieve":
            return qs.prefetch_related(
                Prefetch(
                    "cards",
                    queryset=fetch_cards_qs,
                )
            )
        if self.action == "start_deck":
            return qs.prefetch_related(
                Prefetch(
                    "cards",
                    queryset=fetch_cards_qs.filter(card_state__answered=False),
                )
            )

        return qs

    def get_serializer_class(self):
        if self.action == "create" or self.action == "partial_update":
            return DeckCreateUpdateSerializer
        if self.action == "retrieve":
            return DeckRetrieveSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(
        detail=True,
        methods=["get"],
        serializer_class=DeckRetrieveSerializer,
    )
    def start_deck(self, request: Request, pk=None):
        deck = self.get_object()
        serializer = self.get_serializer(deck)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=["post"],
        url_path="end-deck",
        serializer_class=DeckEndSerializer,
    )
    def end_deck(self, request: Request, pk=None):
        deck = self.get_object()
        user_id = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data["complete"]:
            DeckServices.complete_deck(deck)
            DeckServices.update_deck_statistic(
                qs=self.get_queryset(),
                user_id=user_id,
            )

        return HttpResponseRedirect(redirect_to=reverse("decks-list"))

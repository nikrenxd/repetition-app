from django.db.models import QuerySet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from src.apps.cards.api.serializers import (
    CardSerializer,
    CardCreateUpdateSerializer,
    CardStateSerializer,
)
from src.apps.cards.models import Card
from src.apps.cards.permissions import CardCurrentUserOwnDeckPermission
from src.apps.cards.services import CardService


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated, CardCurrentUserOwnDeckPermission)
    http_method_names = ["get", "post", "delete", "patch"]

    def get_queryset(self):
        qs: QuerySet = super().get_queryset().filter(user=self.request.user)

        if self.action == "list" or self.action == "retrieve":
            return qs.select_related("card_state").prefetch_related("notes")

        return qs

    def get_serializer_class(self):
        if self.action == "create" or self.action == "partial_update":
            return CardCreateUpdateSerializer
        elif self.action == "update_card_state":
            return CardStateSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        card = serializer.save(user=self.request.user)
        CardService.create_card_state(card)

    @action(detail=True, methods=["patch"], url_path="state")
    def update_card_state(self, request: Request, pk: int = None):
        card = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        CardService.update_card_state(card, serializer.validated_data, pk)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

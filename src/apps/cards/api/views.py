from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from src.apps.cards.api.serializers import CardSerializer, CardCreateSerializer
from src.apps.cards.models import Card


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs: QuerySet  = super().get_queryset()

        return qs.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == "create" or self.action == "partial_update":
            return CardCreateSerializer
        
        return super().get_serializer_class()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

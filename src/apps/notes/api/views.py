from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.apps.cards.models import Card
from src.apps.notes.api.serializers import NoteSerializer
from src.apps.notes.models import Note
from src.common.mixins import OwnObjectMixin


class NotesViewSet(OwnObjectMixin, ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs: QuerySet = super().get_queryset()

        return qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        self.own_object("card", Card)
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        self.own_object("card", Card)
        super().perform_update(serializer)

from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.apps.notes.api.serializers import NoteSerializer
from src.apps.notes.models import Note
from src.apps.notes.permissions import NoteCurrentUserOwnCardPermission


class NotesViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated, NoteCurrentUserOwnCardPermission)
    http_method_names = ["get", "post", "delete", "patch"]

    def get_queryset(self):
        qs: QuerySet = super().get_queryset()

        return qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

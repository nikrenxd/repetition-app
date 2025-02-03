from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from src.apps.users.api.serializers import UserCreateSerializer
from src.apps.users.services import UserService
from src.common.mixins import CreateRetrieveUpdateMixin

User = get_user_model()


class UserViewSet(GenericViewSet, CreateRetrieveUpdateMixin):
    """User CRUD endpoints"""

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs: QuerySet = super().get_queryset()

        return qs.filter(id=self.request.user.id)

    def get_permissions(self):
        if self.action == "create":
            return (AllowAny(),)

        return super().get_permissions()

    def perform_create(self, serializer):
        data = serializer.validated_data
        UserService.create_user(User, **data)

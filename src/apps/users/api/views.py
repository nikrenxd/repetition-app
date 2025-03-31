from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from src.apps.users.api.serializers import UserCreateSerializer, UserSerializer
from src.apps.users.services import UserService

User = get_user_model()


class UserViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "post", "delete", "patch"]

    def get_queryset(self):
        qs: QuerySet = super().get_queryset()

        return qs.filter(id=self.request.user.id)

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer

        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "create":
            return (AllowAny(),)

        return super().get_permissions()

    def perform_create(self, serializer):
        data = serializer.validated_data
        user = UserService.create_user(User, **data)
        UserService.create_user_statistic(user)

    @action(detail=False, methods=["GET"])
    def me(self, request):
        user = self.request.user
        serializer = self.get_serializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)

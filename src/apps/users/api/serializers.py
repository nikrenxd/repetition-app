from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from django.contrib.auth import get_user_model

from src.apps.users.models import UserStatistic

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")
        extra_kwargs = {"password": {"write_only": True}}


class UserStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatistic
        fields = (
            "total_decks",
            "completed_decks",
            "completed_decks_percentage",
        )


class EmailLoginSerializer(LoginSerializer):
    username = None


class RegisterSerializerBadRequest(serializers.Serializer):
    detail = serializers.CharField(default="Bad request")

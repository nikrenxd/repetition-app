import pytest
from django.contrib.auth import get_user_model

from src.apps.users.services import UserService

User = get_user_model()


@pytest.mark.django_db
def test_create_user(user_credentials):
    user = UserService.create_user(User, **user_credentials)

    assert user.email == "user1@mail.com"


@pytest.mark.django_db
def test_create_user_statistic(user):
    user_stats = UserService.create_user_statistic(user)

    assert user_stats.user == user


@pytest.mark.django_db
def test_get_user_statistic():
    qs = User.objects.filter(id=1)
    user_stats = UserService.get_user_statistic(qs)

    assert user_stats.total_decks >= 0

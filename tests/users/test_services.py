import pytest
from django.contrib.auth import get_user_model

from src.apps.users.services import UserService

User = get_user_model()


@pytest.mark.django_db
def test_create_user_sevice(user_credentials):
    user = UserService.create_user(User, **user_credentials)

    assert user.email == "user1@mail.com"

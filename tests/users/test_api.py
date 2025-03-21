import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
class TestUserAPI:
    def test_users_create(self, api_client, user_credentials):
        response = api_client.post(reverse("users-list"), data=user_credentials)

        assert response.status_code == 201

    def test_users_retrieve(self, authenticated_client):
        response = authenticated_client.get(reverse("users-detail", kwargs={"pk": 1}))

        assert response.status_code == 200

    def test_users_partial_update(self, authenticated_client):
        data = {"email": "newmail@mail.com"}
        response = authenticated_client.patch(
            reverse("users-detail", kwargs={"pk": 1}),
            data=data,
        )

        assert response.status_code == 200

    def test_users_me(self, authenticated_client):
        response = authenticated_client.get(reverse("users-me"))

        assert response.status_code == 200
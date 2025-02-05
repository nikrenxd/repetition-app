import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
class TestUserAPI:
    def test_create_api(self, api_client, user_credentials):
        response = api_client.post(reverse("users-list"), data=user_credentials)

        assert response.status_code == 201

    def test_retrieve_api(self, authenticated_client):
        response = authenticated_client.get(reverse("users-detail", kwargs={"pk": 1}))

        assert response.status_code == 200

    def test_partial_update_api(self, authenticated_client):
        data = {"email": "newmail@mail.com"}
        response = authenticated_client.patch(
            reverse("users-detail", kwargs={"pk": 1}),
            data=data,
        )

        assert response.status_code == 200

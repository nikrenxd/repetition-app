import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
class TestDeckAPI:
    def test_decks_list(self, authenticated_client):
        response = authenticated_client.get(reverse("decks-list"))

        assert response.status_code == 200

    def test_decks_create(self, authenticated_client):
        data = {"name": "Test Deck 2", "description": "Test"}
        response = authenticated_client.post(reverse("decks-list"), data)

        assert response.status_code == 201

    def test_decks_retrieve(self, authenticated_client):
        response = authenticated_client.get(reverse("decks-detail", kwargs={"pk": 1}))

        assert response.status_code == 200

    def test_decks_update(self, authenticated_client):
        data = {"name": "New Name"}
        response = authenticated_client.patch(
            reverse("decks-detail", kwargs={"pk": 1}), data
        )

        assert response.status_code == 200

    def test_decks_delete(self, authenticated_client):
        response = authenticated_client.delete(reverse("decks-detail", kwargs={"pk": 1}))

        assert response.status_code == 204
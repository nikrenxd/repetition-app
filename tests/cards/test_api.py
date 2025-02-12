import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
class TestCardAPI:
    def test_cards_list(self, authenticated_client):
        response = authenticated_client.get(reverse("cards-list"))

        assert response.status_code == 200

    def test_cards_details(self, authenticated_client):
        response = authenticated_client.get(reverse("cards-detail", kwargs={"pk": 1}))

        assert response.status_code == 200

    def test_cards_create(self, authenticated_client):
        data = {
            "question": "test question 2",
            "answer": "test answer 2",
            "deck": 1,
        }

        response = authenticated_client.post(reverse("cards-list"), data=data)

        assert response.status_code == 201

    def test_cards_update(self, authenticated_client):
        data = {
            "question": "updated question",
        }

        response = authenticated_client.patch(
            reverse("cards-detail", kwargs={"pk": 1}), data=data
        )

        assert response.status_code == 200

    def test_cards_delete(self, authenticated_client):
        response = authenticated_client.delete(
            reverse("cards-detail", kwargs={"pk": 1})
        )

        assert response.status_code == 204

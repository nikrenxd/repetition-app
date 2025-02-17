import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
class TestNotesApi:
    def test_notes_list(self, authenticated_client):
        response = authenticated_client.get(reverse("notes-list"))

        assert response.status_code == 200

    def test_notes_create(self, authenticated_client):
        data = {"content": "test note", "card": 1}
        response = authenticated_client.post(reverse("notes-list"), data=data)

        assert response.status_code == 201

    def test_notes_detail(self, authenticated_client):
        response = authenticated_client.get(
            reverse("notes-detail", kwargs={"pk": 1}),
        )

        assert response.status_code == 200

    def test_notes_update(self, authenticated_client):
        data = {
            "content": "note 1",
            "card": 1,
        }
        response = authenticated_client.patch(
            reverse("notes-detail", kwargs={"pk": 1}), data=data
        )

        assert response.status_code == 200

    def test_notes_delete(self, authenticated_client):
        response = authenticated_client.delete(
            reverse("notes-detail", kwargs={"pk": 1})
        )

        assert response.status_code == 204

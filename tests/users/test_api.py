import pytest
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_create_api(api_client, user_credentials):
    response = api_client.post(reverse("users-list"), data=user_credentials)

    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_api(authenticated_client):
    response = authenticated_client.get(reverse("users-detail", kwargs={"pk": 1}))

    assert response.status_code == 200


@pytest.mark.django_db
def test_partial_update_api(authenticated_client):
    data = {"email": "newmail@mail.com"}
    response = authenticated_client.patch(
        reverse("users-detail", kwargs={"pk": 1}),
        data=data,
    )

    assert response.status_code == 200

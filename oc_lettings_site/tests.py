import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_index_view(client):
    """Test the main index view"""
    response = client.get(reverse("index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_404_error_view(client):
    """Test the main index view"""
    response = client.get('wrong-url')
    assert response.status_code == 404
    assert "Error 404" in response.content.decode()

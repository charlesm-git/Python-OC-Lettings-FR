import pytest
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_model():
    """Test the Address model"""
    address = Address.objects.create(
        number=1,
        street="Test Street",
        city="Test City",
        state="20",
        zip_code=20246,
        country_iso_code=123,
    )
    assert address.city == "Test City"
    assert str(address) == f"{address.number} {address.street}"


@pytest.mark.django_db
def test_letting_model():
    """Test the Letting model"""
    address = Address.objects.create(
        number=1,
        street="Test Street",
        city="Test City",
        state="20",
        zip_code=20246,
        country_iso_code=123,
    )
    letting = Letting.objects.create(title="test Title", address=address)
    assert str(letting) == letting.title
    assert letting.address.city == "Test City"


@pytest.mark.django_db
def test_lettings_index_view(client):
    """Test the letting index view"""
    response = client.get(reverse("lettings_index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_detail_view(client):
    """Test the letting detail view"""
    address = Address.objects.create(
        number=1,
        street="Test Street",
        city="Test City",
        state="20",
        zip_code=20246,
        country_iso_code=123,
    )
    letting = Letting.objects.create(title="test Title", address=address)
    response = client.get(
        reverse("letting", kwargs={"letting_id": letting.id})
    )
    assert response.status_code == 200

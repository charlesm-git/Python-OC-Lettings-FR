import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db
def test_profile_model():
    """Test the profile model"""
    user = User.objects.create(username="Test", password="password")
    profile = Profile.objects.create(user=user, favorite_city="Test City")
    assert profile.favorite_city == "Test City"
    assert str(profile) == profile.user.username


@pytest.mark.django_db
def test_profiles_index_view(client):
    """Test the profiles index view"""
    response = client.get(reverse("profiles_index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_detail_view(client):
    """Test the profile detail view"""
    user = User.objects.create(username="Test", password="password")
    profile = Profile.objects.create(user=user)
    response = client.get(
        reverse("profile", kwargs={"username": profile.user.username})
    )
    assert response.status_code == 200

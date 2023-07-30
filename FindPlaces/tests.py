import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Place

@pytest.mark.django_db
class TestPlaceViews:

    @pytest.fixture
    def api_client(self):
        print("jkkkkkk")
        return APIClient()

    @pytest.fixture
    def place_data(self):
        print("kkkkkk")
        return {
            "name": "Test Place",
            "description": "A test place",
            "latitude": 40.7128,
            "longitude": -74.0060,
        }

    def test_place_list_create_view(self, api_client, place_data):
        url = reverse("place-list-create")
        response = api_client.post(url, place_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Place.objects.count() == 1
        assert Place.objects.get().name == place_data['name']

    def test_place_search_view(self, api_client, place_data):
        Place.objects.create(**place_data)

        url = reverse("place-search")
        response = api_client.get(url, {"query": "Test"})
        assert response.status_code == status.HTTP_200_OK
        assert response.data[0]["name"] == place_data["name"]

    def test_place_list_template_rendering(self, api_client):
        url = reverse("place-list")
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert "Place List" in response.content.decode("utf-8")

    def test_map_integration_and_dynamic_search(self, api_client):
        url = reverse("place-list")
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert 'id="map"' in response.content.decode("utf-8")
        assert 'id="search-form"' in response.content.decode("utf-8")
        assert 'id="search-input"' in response.content.decode("utf-8")

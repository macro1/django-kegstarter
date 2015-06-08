import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from .. import django_factories
from . import factories


@pytest.mark.django_db
def test_staff_can_add_beer():
    user = django_factories.UserFactory(is_staff=True)
    brewer = factories.BrewerFactory()
    beer = factories.BeerFactory(brewer=brewer)
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"brewer": brewer.id,
            "name": beer.name,
            "abv": beer.abv}
    response = client.post(reverse('beer-beer-list'), data=data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_non_staff_cannot_add_beer():
    user = django_factories.UserFactory()
    brewer = factories.BrewerFactory()
    beer = factories.BeerFactory(brewer=brewer)
    client = APIClient()
    client.force_authenticate(user=user)
    data = {"brewer": reverse('beer-brewer-detail', kwargs={'pk': brewer.id}),
            "name": beer.name, "abv": beer.abv}
    response = client.post(reverse('beer-beer-list'), data=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_staff_can_edit_brewer():
    user = django_factories.UserFactory(is_staff=True)
    brewer = factories.BrewerFactory()
    old_brewer_name = brewer.name
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.put(reverse('beer-brewer-detail', kwargs={'pk': brewer.id}),
                          data={"name": 'new_{}'.format(old_brewer_name)})
    assert response.data['name'] == 'new_{}'.format(old_brewer_name)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_non_staff_cannot_edit_brewer():
    user = django_factories.UserFactory()
    brewer = factories.BrewerFactory()
    old_brewer_name = brewer.name
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.put(reverse('beer-brewer-detail', kwargs={'pk': brewer.id}),
                          data={"name": 'new_{}'.format(old_brewer_name)})
    assert brewer.name != 'new_{}'.format(old_brewer_name)
    assert response.status_code == status.HTTP_403_FORBIDDEN

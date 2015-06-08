import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from kegstarter.keg.models import Keg
from .. import django_factories
from . import factories


@pytest.mark.django_db
def test_staff_can_delete_keg():
    user = django_factories.UserFactory(is_staff=True)
    keg = factories.KegFactory()
    client = APIClient()
    client.force_authenticate(user=user)
    original_keg_count = Keg.objects.all().count()
    response = client.delete(reverse('keg-keg-detail', kwargs={'pk': keg.id}))
    new_keg_count = Keg.objects.all().count()
    assert new_keg_count == original_keg_count - 1
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_non_staff_cannot_delete_keg():
    user = django_factories.UserFactory()
    keg = factories.KegFactory()
    client = APIClient()
    client.force_authenticate(user=user)
    original_keg_count = Keg.objects.all().count()
    response = client.delete(reverse('keg-keg-detail', kwargs={'pk': keg.id}))
    new_keg_count = Keg.objects.all().count()
    assert new_keg_count == original_keg_count
    assert response.status_code == status.HTTP_403_FORBIDDEN

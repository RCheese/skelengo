import pytest
from rest_framework.test import APIRequestFactory

from skelengo.probes.views import LivenessProbe, ReadnessProbe

factory = APIRequestFactory()


def test_liveness():
    request = factory.get("/probes/liveness/")
    view = LivenessProbe.as_view()
    response = view(request)
    assert response.data == "ok"


@pytest.mark.django_db
def test_readness():
    request = factory.get("/probes/readness/")
    view = ReadnessProbe.as_view()
    response = view(request)
    assert response.data == "ok"

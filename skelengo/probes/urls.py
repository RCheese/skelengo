from django.urls import path

from .views import LivenessProbe, ReadnessProbe

urlpatterns = [
    path("readness/", ReadnessProbe.as_view(), name="readness"),
    path("liveness/", LivenessProbe.as_view(), name="liveness"),
]

from rest_framework import routers

from .views import ShipView

router = routers.SimpleRouter()
router.register("ship", ShipView, basename="ship")

urlpatterns = []
urlpatterns += router.urls

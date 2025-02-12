from rest_framework.routers import DefaultRouter

from src.apps.cards.api.views import CardViewSet

router = DefaultRouter()

router.register("cards", CardViewSet, basename="cards")

urlpatterns = router.urls
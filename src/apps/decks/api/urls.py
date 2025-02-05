from rest_framework import routers

from src.apps.decks.api.views import DeckViewSet

router = routers.DefaultRouter()

router.register("decks", DeckViewSet, basename="decks")

urlpatterns = router.urls

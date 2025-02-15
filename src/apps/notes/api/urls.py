from rest_framework.routers import DefaultRouter

from src.apps.notes.api.views import NotesViewSet

router = DefaultRouter()

router.register("notes", NotesViewSet, basename="notes")

urlpatterns = router.urls

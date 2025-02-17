from django.db.models import Model
from rest_framework.exceptions import NotFound
from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)

from src.common.services import user_owns_object


class CreateRetrieveUpdateMixin(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    pass


class OwnObjectMixin:
    def own_object(self, obj_name: str, model: Model):
        """Utilize user_owns_object to check if a current user owns a given object"""
        is_own = user_owns_object(obj_name, model, self.request)

        if not is_own:
            raise NotFound

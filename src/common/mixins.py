from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
)


class CreateRetrieveUpdateMixin(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    pass

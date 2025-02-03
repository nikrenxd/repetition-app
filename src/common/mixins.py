from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
)


class UpdateDestroyMixin(UpdateModelMixin, DestroyModelMixin):
    pass


class RetrieveUpdateDestroyMixin(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    pass


class CreateRetrieveUpdateMixin(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
):
    pass

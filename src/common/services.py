from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from django.db.models import Model


def user_owns_object(obj_name: str, model: Model, request: Request) -> bool:
    """Checks if object is owned by current user"""

    obj_id = request.data.get(obj_name, None)

    if not obj_id:
        return False

    obj = get_object_or_404(model, pk=obj_id)

    return request.user == obj.user

from rest_framework import permissions
from rest_framework.generics import get_object_or_404

CHECK_METHODS = ["POST", "PATCH", "PUT"]


class CurrentUserOwnObjectPermission(permissions.BasePermission):
    obj_name_in_request = None
    model = None

    def has_permission(self, request, view):
        """Check if user owns a related object"""

        if request.method not in CHECK_METHODS:
            return True

        obj_id = request.data.get(self.obj_name_in_request, None)

        obj = get_object_or_404(self.model, pk=obj_id)

        return request.user == obj.user

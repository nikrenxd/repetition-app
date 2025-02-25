from rest_framework import permissions
from rest_framework.generics import get_object_or_404


class CurrentUserOwnObjectPermission(permissions.BasePermission):
    obj_name_in_request = None
    model = None

    def has_permission(self, request, view):
        obj_id = request.data.get(self.obj_name_in_request, None)

        if not obj_id:
            return False

        obj = get_object_or_404(self.model, pk=obj_id)

        return request.user == obj.user

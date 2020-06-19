from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = "Not Authenticated"

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        try:
            return obj.projectCreator == request.user
        except AttributeError:
            try:
                return obj.setCreator == request.user
            except AttributeError:
                return obj.creator == request.user
        return False

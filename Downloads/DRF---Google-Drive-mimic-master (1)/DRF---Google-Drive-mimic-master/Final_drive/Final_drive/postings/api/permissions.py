from rest_framework import permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user

class IsAdmin(permissions.BasePermission):
    """Allow access to admins"""
    def has_object_permission(self, request, view, obj):
        return request.user.is_admin()


class IsOwner(permissions.BasePermission):
    """Allow access to owners"""
    def has_object_permission(self, request, view, obj):
        request.user.is_owner(obj)


class IsAdminOrOwner(permissions.BasePermission):
    """Allow access to admins and owners"""
    def has_object_permission(*args):
        return (IsAdmin.has_object_permission(*args) or
                IsOwner.has_object_permission(*args))

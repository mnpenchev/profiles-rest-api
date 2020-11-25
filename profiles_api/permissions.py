from rest_framework import permissions


class UpdateOwnPermissions(permissions.BasePermission):
    """ Allow user to edit their own proffile """

    def has_object_permission(self, request, view, obj):
        """ check if user is trying to edit their own profile  """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


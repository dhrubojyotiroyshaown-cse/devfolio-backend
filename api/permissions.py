from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Allow everyone to read public data.
    Only authenticated admin/staff users can create,
    update, or delete data.
    """

    def has_permission(self, request, view):
        # Allow read-only requests: GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return True

        # Only authenticated staff users can modify data
        return (
            request.user.is_authenticated
            and request.user.is_staff
        )
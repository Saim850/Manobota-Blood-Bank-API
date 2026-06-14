from rest_framework import permissions

permissions.IsAuthenticated
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        else:
            return False

class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user == obj.user:
            return True
        else:
            return False

            
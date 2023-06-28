from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "permission denied , you are not the owener"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


# بررسی کاربری که میخواهد عملیات جدیدی انجام دهد و کاربری که آن مدل یا اطلاعات را از اول ایجاد کرده است.

class IsOwnerOrReadOnlyDelete(BasePermission):
    message = "Permission denied!!!"

    def has_permission(self, request, view):
        return request.user.is_Authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
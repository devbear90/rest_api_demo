from rest_framework import permissions

# object level custom permission example
class IsPostAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
from rest_framework import permissions
from .models import APIKey
from datetime import datetime


# object level custom permission example
class IsPostAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
    

class IsInEditorsGroup(permissions.BasePermission):
    """
    Django group permission example: custom userrel
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Editors').exists()
    
class IsAdminOrChangeOnly(permissions.BasePermission):
    """
    Csak admin törölhet, mindenki más olvashat vagy módosíthat.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        """
            Csak a DELETE-et vizsgálom, ebben az esetben minden más: PUT, PATCH, POST engedélyezett 
                -> csak a példa miatt
         """
        if request.method == 'DELETE':
            return request.user and request.user.is_staff
        return True
    
    # Ez lenne egy olyan példa, ahol az utasításokat jogosultságokkal együtt "szétszedjük"
    def has_object_permission2(self, request, view, obj):
        if request.method == 'DELETE':
            return request.user and request.user.is_staff
        if request.method in ['PATCH', 'PUT']:
            return obj.author == request.user or request.user.is_staff
        return True

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Csak a saját feladataidhoz férhetsz hozzá - kivéve, ha admin vagy.
    """

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        # A nem adminok csak a saját rekordjukhoz férnek hozzá
        return obj.assigned_to == request.user
    
class IsWorkingHours(permissions.BasePermission):
    """
    Csak hétköznap 9:00 - 17:00 között engedélyezett nem-admin felhasználóknak.
    """

    def has_permission(self, request, view):
        user = request.user

        # Admin bármikor hozzáfér
        if user.is_staff:
            return True

        now = datetime.now()
        # hétfő=0 - péntek=4
        is_weekday = now.weekday() < 5  
        is_working_hour = 12 <= now.hour < 17

        return is_weekday and is_working_hour
    
class HasTrustedHeader(permissions.BasePermission):
    """
    Csak akkor engedélyezett, ha a kérés tartalmaz egy 'X-ACCESS-LEVEL: trusted' fejlécet.
    """

    def has_permission(self, request, view):
        access_level = request.headers.get('X-ACCESS-LEVEL')
        return access_level == 'trusted'
    
class HasValidAPIKeyFromDB(permissions.BasePermission):
    """
    Csak akkor engedélyezett, ha a fejlécben szereplő kulcs szerepel az adatbázisban és aktív.
    """

    def has_permission(self, request, view):
        key = request.headers.get('X-API-KEY')
        return APIKey.objects.filter(key=key, is_active=True).exists()
    
class HasValidAPIKeyFromDB(permissions.BasePermission):
    """
    Csak akkor engedélyezett, ha a kérésben szereplő kulcs benne van az adatbázisban és aktív.
    """

    def has_permission(self, request, view):
        key = request.headers.get('X-API-KEY')
        return APIKey.objects.filter(key=key, is_active=True).exists()
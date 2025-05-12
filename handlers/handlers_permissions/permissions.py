from handlers import *

class IsAdminPermissionHandler(BasePermission):
    async def has_permission(self):
        """Check if the user is an admin."""
        if self.user.is_admin == 1:
            return await super().has_permission()
        return False

class IsActiveUserPermissionHandler(BasePermission):
    async def has_permission(self):
        """Check if the user is active."""
        if self.user.is_active == 1:
            return await super().has_permission()
        return False

class IsSpecialUserPermissionHandler(BasePermission):
    async def has_permission(self):
        """Check if the user is a special user."""
        if self.user.is_special == 1:
            return await super().has_permission()
        return False
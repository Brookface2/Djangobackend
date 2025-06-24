from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    def has_module_permission(self, request):
        return request.user.is_superuser or request.user.role == 'admin'

admin.site.register(User, UserAdmin)
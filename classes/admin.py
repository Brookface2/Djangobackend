from django.contrib import admin
from .models import Booking, GymClass
from django.contrib.auth import get_user_model

User = get_user_model()

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'coach')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role == 'coach':
            return qs.filter(coach=request.user)
        return qs

    def has_change_permission(self, request, obj=None):
        if request.user.role == 'coach' and obj and obj.coach != request.user:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return request.user.role != 'coach'

admin.site.register(GymClass, ClassAdmin)
admin.site.register(Booking)

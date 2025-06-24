from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_redirect_view, name='dashboard'),
    path('admin/', views.admin_dashboard_view, name='admin_dashboard'),
    path('coach/', views.coach_dashboard_view, name='coach_dashboard'),
    path('member/', views.member_dashboard_view, name='member_dashboard'),
]
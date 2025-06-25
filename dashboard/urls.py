from django.urls import path
from . import views

urlpatterns = [
    path('role/', views.dashboard_role_view, name='dashboard_role'),
]
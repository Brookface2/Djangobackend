from django.urls import path
from .views import (
    ClassCreateView, ClassListView, ClassDetailView,
    BookingCreateView, BookingListView
)

urlpatterns = [
    path('classes/', ClassListView.as_view(), name='class-list'),
    path('classes/create/', ClassCreateView.as_view(), name='class-create'),
    path('classes/<int:pk>/', ClassDetailView.as_view(), name='class-detail'),
    path('bookings/', BookingListView.as_view(), name='booking-list'),
    path('bookings/create/', BookingCreateView.as_view(), name='booking-create'),
]

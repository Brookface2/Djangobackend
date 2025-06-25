from django.urls import path
from .views import BookingListCreateView, BookingDetailView

urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking-list-create'),           # GET/POST /api/v1/bookings/
    path('<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),           # GET/PUT/DELETE /api/v1/bookings/<id>/
]
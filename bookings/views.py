from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView

from .models import Booking
from .serializers import BookingSerializer
from users.permissions import IsCoachOrAdmin, IsAdminOrClassCoach

class BookingListView(ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(member=self.request.user)

    def get_serializer_context(self):
        return {"request": self.request}


class BookingCreateView(CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}

    def perform_create(self, serializer):
        serializer.save(member=self.request.user)
from users.permissions import IsAdmin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsCoach, IsAdmin
from rest_framework import status

class AdminNotificationView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        # Admin sending forms or announcements
        return Response({"message": "Notification sent"})

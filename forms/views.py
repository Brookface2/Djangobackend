from users.permissions import IsMember
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsMember

class FormSubmitView(APIView):
    permission_classes = [IsAuthenticated, IsMember]

    def post(self, request):
        # Logic to submit form
        return Response({"message": "Form submitted"})
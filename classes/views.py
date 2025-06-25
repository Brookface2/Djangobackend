from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from .models import GymClass
from .serializers import GymClassSerializer
from users.permissions import IsCoachOrAdmin, IsAdminOrClassCoach

class ClassCreateView(CreateAPIView):
    queryset = GymClass.objects.all()
    serializer_class = GymClassSerializer
    permission_classes = [IsAuthenticated, IsCoachOrAdmin]

    def get_serializer_context(self):
        return {"request": self.request}

    def perform_create(self, serializer):
        user = self.request.user
        if user.role == 'coach':
            # Force coach to be logged-in user
            serializer.save(coach=user)
        else:
            serializer.save()


class ClassListView(ListAPIView):
    queryset = GymClass.objects.all()
    serializer_class = GymClassSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}


class ClassDetailView(RetrieveUpdateDestroyAPIView):
    queryset = GymClass.objects.all()
    serializer_class = GymClassSerializer
    permission_classes = [IsAuthenticated, IsAdminOrClassCoach]

    def get_serializer_context(self):
        return {"request": self.request}


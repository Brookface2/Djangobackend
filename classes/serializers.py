from rest_framework import serializers
from .models import GymClass

class GymClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymClass
        fields = ['id', 'name', 'description', 'start_time', 'coach', 'capacity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        if user.role == 'coach':
            # Coaches cannot assign coach manually
            self.fields['coach'].read_only = True

    def validate_coach(self, value):
        if value.role != 'coach':
            raise serializers.ValidationError("Assigned user is not a coach.")
        return value
from rest_framework import serializers
from .models import GymClass, Booking

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


class BookingSerializer(serializers.ModelSerializer):
    member = serializers.ReadOnlyField(source='member.username')

    class Meta:
        model = Booking
        fields = ['id', 'member', 'gym_class', 'timestamp', 'attended']
        read_only_fields = ['timestamp', 'member']

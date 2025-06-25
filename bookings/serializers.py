from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    member = serializers.ReadOnlyField(source='member.username')
    gym_class = serializers.SlugRelatedField(
        slug_field='name',  # or another field from GymClass
        queryset=None  # Set this in __init__ if needed
    )

    class Meta:
        model = Booking
        fields = ['id', 'member', 'gym_class', 'timestamp', 'attended']
        read_only_fields = ['timestamp', 'member']

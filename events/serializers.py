from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id', 
            'title', 
            'discription', 
            'image', 
            'venue_name',
            'venue_address',
            'start_datetime',
            'end_datetime'
        ]
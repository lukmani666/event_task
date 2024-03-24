from django.shortcuts import render, get_object_or_404
from rest_framework import status
from .serializers import EventSerializer
from .models import Event
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

    
class EventList(APIView):
    def get(self, request, format=None):
        time = timezone.now()
        upcoming_events = Event.objects.filter(start_datetime__gt=time)
        active_events = Event.objects.filter(start_datetime__lte=time, end_datetime__gte=time)
        past_events = Event.objects.filter(end_datetime__lt=time)

        upcoming_serializer = EventSerializer(upcoming_events, many=True)
        active_serializer = EventSerializer(active_events, many=True)
        past_serializer = EventSerializer(past_events, many=True)

        return Response({
            'upcoming-events': upcoming_serializer.data,
            'active-events': active_serializer.data,
            'past-event': past_serializer.data
        })

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EventDetail(APIView):
    def get(self, request, pk, format=None):
        event = get_object_or_404(Event.objects.all(), pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        event = get_object_or_404(Event.objects.all(), pk=pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    def get(self, request, format=None):
        return Response({'success': 'CSRF cookie set'})




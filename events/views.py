from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from designerhub.permissions import IsOwnerOrReadOnly
from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all().order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = {
        "owner__followed__owner__profile": ["exact"],
        "owner__profile": ["exact"],
        'event_date': ['lte'],
    }
    search_fields = [
        "owner__username",
        "title",
        "event_date",
        "tags__name",
    ]
    ordering_fields = []

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.all().order_by("-created_at")


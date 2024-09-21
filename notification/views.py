from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Notification
from .serializers import NotificationSerializer

class NotificationList(generics.ListAPIView):
    """
    List of notifications view for authenticated user.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(recipient=self.request.user)

class NotificationUpdate(generics.UpdateAPIView):
    """
    Update view for a specific notifcication.
    """
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
from rest_framework import generics, permissions
from .models import Favorite
from .serializers import FavoriteSerializer
from django.contrib.contenttypes.models import ContentType

class FavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        content_type = ContentType.objects.get_for_model(serializer.validated_data['content_object'])
        serializer.save(user=self.request.user, content_type=content_type)


class FavoriteDeleteView(generics.DestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        content_type = ContentType.objects.get_for_model(self.kwargs['model'])
        return Favorite.objects.filter(user=self.request.user, content_type=content_type, object_id=self.kwargs['object_id'])

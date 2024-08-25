from rest_framework import serializers
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'content_type', 'object_id', 'added_at']
        read_only_fields = ['id', 'user', 'added_at']

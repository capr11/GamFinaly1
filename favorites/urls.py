from django.urls import path
from .views import FavoriteListCreateView, FavoriteDeleteView

urlpatterns = [
    path('favorites/', FavoriteListCreateView.as_view(), name='favorite-list-create'),
    path('favorites/<str:model>/<int:object_id>/', FavoriteDeleteView.as_view(), name='favorite-delete'),
]

from unicodedata import category
from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework import generics, permissions
from .models import Category, Image, Game
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from .serializers import ImageListSerializer, CategoryListSerializer, GameDetailSerializer, GameListSerializer, \
    CategorySerializer, ImageSerializer, GameSerializer
from rest_framework.pagination import PageNumberPagination


class MainPageView(APIView):
    def get(self, request):
        try:
            # Получаем все игры и категории
            games = Game.objects.all()
            categories = Category.objects.all()

            # Сериализуем данные
            games_serializer = GameListSerializer(games, many=True)
            categories_serializer = CategoryListSerializer(categories, many=True)

            # Формируем ответ
            return Response({
                'games': games_serializer.data,
                'categories': categories_serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class GameFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__title', lookup_expr='icontains')
    title = filters.CharFilter(lookup_expr='icontains')
    created_date = filters.DateFromToRangeFilter()

    class Meta:
        model = Game
        fields = ['category', 'title', 'created_date']



class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = GameFilter
    search_fields = ['title', 'description']
    ordering_fields = ['created_date', 'title']
    pagination_class = PageNumberPagination


class GameDetailView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameDetailSerializer

    def get(self, request, *args, **kwargs):
        game = self.queryset.first()

        game_serializer = GameDetailSerializer(game)

        recommended_games = Game.objects.filter(category=game.category).exclude(id=game.id)

        recommended_games_serializer = GameListSerializer(recommended_games, many=True)

        return  Response({
            "detail":game_serializer.data,
            "recommended_games":recommended_games_serializer.data

        })


       # CRUD
class IsAdminUser(permissions.BasePermission):
    """
    Разрешение, позволяющее доступ только администраторам.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUser]

class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAdminUser]

class GameListCreateView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAdminUser]

class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAdminUser]
    filterset_fields = ['category__title', 'title', 'created_date']
    search_fields = ['title', 'description']
    ordering_fields = ['created_date', 'updated_date']

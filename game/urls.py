from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.MainPageView.as_view()),
    path('index/<int:pk>/', views.GameDetailView.as_view()),
    path('game_list/', views.GameListView.as_view()),
    path('categories/', views.CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view()),
    path('images/', views.ImageListCreateView.as_view()),
    path('images/<int:pk>/', views.ImageDetailView.as_view()),
    path('games/', views.GameListCreateView.as_view()),


]

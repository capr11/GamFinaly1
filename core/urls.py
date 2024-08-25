from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

schema_view = get_schema_view(
   openapi.Info(
      title="GameFinaly API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include('favorites.urls')),
    path('api/', include('game.urls')),
    path('api/', include('user.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title='DRF-lab API',
        default_version='v1',
        description='Documentation of DRF-lab API',
        contact=openapi.Contact(email="edgarpo0401@gmail.com"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('docs/', schema_view.with_ui('swagger')),
]

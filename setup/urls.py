from django.contrib import admin
from django.urls import path, include
from api.views import CedentesViewSet, BancosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cedentes', CedentesViewSet, basename='Cedentes')
router.register('bancos', BancosViewSet, basename='Bancos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

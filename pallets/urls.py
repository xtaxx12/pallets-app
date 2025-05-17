from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PalletViewSet

router = DefaultRouter()
router.register(r'pallets', PalletViewSet, basename='pallet')

urlpatterns = [
    path('', include(router.urls)),
]

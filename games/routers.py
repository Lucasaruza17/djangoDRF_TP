from rest_framework.routers import DefaultRouter
from .views import GameViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet, basename='game')
router.register(r'categories', CategoryViewSet, basename='category')
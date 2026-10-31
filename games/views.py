from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import Game, Category
from .serializers import GameSerializer, CategorySerializer

# ReadOnlyModelViewSet: Solo permite GET (listar y detalle)
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny] # Cualquiera puede ver las categorías

# ModelViewSet: Permite el CRUD completo
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    # Solo los usuarios logueados (con JWT) pueden crear, actualizar o borrar. 
    # Los no logueados solo pueden ver (GET)
    permission_classes = [IsAuthenticatedOrReadOnly]
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .routers import router

urlpatterns = [
    # Incluimos las rutas generadas automáticamente por los ViewSets
    path('', include(router.urls)),
    
    # Endpoints para la autenticación con JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
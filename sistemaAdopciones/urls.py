from django.urls import path
from .views import (
    AnimalListAPIView, 
    UsuarioListAPIView, 
    SolicitudAdopcionListAPIView,
    RegistroUsuarioView,
    SolicitudAdopcionListCreate,
    SolicitudAdopcionUpdate,
    PerfilAdoptanteView,
    EjemploView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('api/animales/', AnimalListAPIView.as_view(), name='animales_api'),
    path('api/usuarios/', UsuarioListAPIView.as_view(), name='usuarios_api'),
    path('api/solicitudes/', SolicitudAdopcionListAPIView.as_view(), name='solicitudes_api'),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/usuarios/registro', RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('solicitudes/<int:pk>/', SolicitudAdopcionUpdate.as_view(), name='solicitud_update'),
    path('api/perfil/', PerfilAdoptanteView.as_view(), name='perfil-adoptante'),
    path('api/ejemplo/', EjemploView.as_view(), name='perfil-ejemplo'),
]
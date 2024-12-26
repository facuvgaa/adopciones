from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AnimalListAPIView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name= 'login'),
    path('api/animales/', AnimalListAPIView.as_view(), name='animales_api'),
]
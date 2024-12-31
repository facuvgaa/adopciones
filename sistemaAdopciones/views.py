from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Animal , Usuario, SolicitudAdopcion
from .serializers import AnimalSerializer , UsuarioSerializer , SolicitudAdopcionSerializer, RegistroUsuarioSerializer

class SolicitudAdopcionListCreate(APIView):
    def get(self, request):
        # Listar todas las solicitudes de adopción
        solicitudes = SolicitudAdopcion.objects.all()
        serializer = SolicitudAdopcionSerializer(solicitudes, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Crear una nueva solicitud de adopción
        serializer = SolicitudAdopcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Solicitud de adopción creada exitosamente",
                "solicitudId": serializer.data['id']
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SolicitudAdopcionUpdate(APIView):
    def put(self, request, pk):
        try:
            solicitud = SolicitudAdopcion.objects.get(pk=pk)
        except SolicitudAdopcion.DoesNotExist:
            return Response({"message": "Solicitud no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        if solicitud.estado != "PENDIENTE" and request.data.get("estado") in ["APROBADA", "RECHAZADA"]:
            return Response({"message": "Solo se pueden actualizar solicitudes pendientes."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SolicitudAdopcionSerializer(solicitud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Estado de solicitud actualizado",
                "estado": serializer.data['estado']
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = RegistroUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response({
                "message": "Usuario registrado exitosamente",
                "userId": usuario.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnimalListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        
        animales = Animal.objects.all()
        serializer = AnimalSerializer(animales, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioListAPIView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SolicitudAdopcionListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        solicitudes = SolicitudAdopcion.objects.all()
        serializer = SolicitudAdopcionSerializer(solicitudes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SolicitudAdopcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PerfilAdoptanteView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados

    def get(self, request):
        usuario = request.user  # Usuario autenticado
        return Response({
            "id": usuario.id,
            "username": usuario.username,
            "email": usuario.email,
            # Agrega otros campos necesarios aquí
        })

class EjemploView(APIView):
    

    def get(self, request):
        # Tu lógica para devolver el perfil
        return Response({"profile": "data"})

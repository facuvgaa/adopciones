from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Animal , Usuario, SolicitudAdopcion
from .serializers import AnimalSerializer , UsuarioSerializer , SolicitudAdopcionSerializer


class AnimalListAPIView(APIView):
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

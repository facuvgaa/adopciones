from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Animal
from .serializers import AnimalSerializer


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

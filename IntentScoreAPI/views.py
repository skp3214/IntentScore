from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductOfferSerializer

@api_view(['POST'])
def create_offer(request):
    serializer = ProductOfferSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
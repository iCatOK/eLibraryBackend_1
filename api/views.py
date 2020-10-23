from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
# Create your views here.

"""
class UserList(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
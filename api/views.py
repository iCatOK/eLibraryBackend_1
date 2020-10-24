from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book, User
from .serializers import BookSerializer, UserSerializer
from rest_framework import serializers, generics
from .permissions import IsLibrarianOrNothing


# Create your views here.
class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"Books": serializer.data})

    def post(self, request):
        serializer = BookSerializer(data=request.data.get('book'))

        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()

        return Response({"Success": "Book {} created successfully".format(book_saved.name)})
      

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        IsLibrarianOrNothing,
    ]

class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        IsLibrarianOrNothing
    ]


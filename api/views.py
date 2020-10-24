from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Book, Genre, Branch
from .serializers import UserSerializer, BookSerializer, GenreSerializer, BranchSerializer
from rest_framework import serializers, generics
from .permissions import IsLibrarianOrNothing


# Create your views here.

class BookListView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class GenreListView(generics.ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class BranchListView(generics.ListCreateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()


class BookDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BranchDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()


class GenreDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()




# class BookView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response({"Books": serializer.data})

#     def post(self, request):
#         serializer = BookSerializer(data=request.data.get('book'))

#         if serializer.is_valid(raise_exception=True):
#             book_saved = serializer.save()

#         return Response({"Success": "Book {} created successfully".format(book_saved.name)})
      

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


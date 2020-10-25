from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Book, Genre, Branch, Order, BookTransaction
from .serializers import UserSerializer, BookSerializer, \
GenreSerializer, BranchSerializer, OrderSerializer, BookTransactionSerilizer

from rest_framework import serializers, generics
from .permissions import IsLibrarianOrNothing


# Create your views here.

class LibrarianBookListView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     if not request.user.is_librarian:
        #         raise serializers.ValidationError({"error":"You don't have permissions"})
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        # if request.user.is_authenticated:
        #     if not request.user.is_librarian:
        #         raise serializers.ValidationError({"error":"You don't have permissions"})
        return self.create(request, *args, **kwargs)

class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_queryset(self):
        current_user = self.request.user
        return Book.objects.filter(branch=current_user.branch)

class OrderListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class GenreListView(generics.ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class BranchListView(generics.ListCreateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()


class BookTransactionListView(generics.ListCreateAPIView):
    serializer_class = BookTransactionSerilizer
    queryset = BookTransaction.objects.all()


class BookDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BranchDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()


class GenreDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class OrderDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class BookTransactionDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = BookTransactionSerilizer
    queryset = BookTransaction.objects.all()
     

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [
    #     IsLibrarianOrNothing,
    # ]

class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [
    #     IsLibrarianOrNothing
    # ]


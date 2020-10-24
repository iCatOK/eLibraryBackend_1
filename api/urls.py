from django.urls import path

import api.views as views
from django.urls import path, include

app_name = 'api'

user_patterns = [
    path('', views.UserListView.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]

book_patterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]

branch_patterns = [
    path('', views.BranchListView.as_view(), name='branch-list'),
    path('<int:pk>/', views.BranchDetailView.as_view(), name='branch-detail'),
]

genre_patterns = [
    path('', views.GenreListView.as_view(), name='genre-list'),
    path('<int:pk>/', views.GenreDetailView.as_view(), name='genre-detail'),
]


urlpatterns = [
    path('users/', include(user_patterns)),
    path('books/', include(book_patterns)),
    path('branches/', include(branch_patterns)),
    path('genres/', include(genre_patterns)),
]
from django.urls import path
from .views import BookView

app_name = "books"

urlpatterns = [
    path('books/', BookView.as_view()),
]
from django.contrib import admin
from django.urls import path, include
from .views import get_books, get_book

urlpatterns = [
    path('books/', get_books, name='get_books'),
    path('books/<int:book_id>', get_book, name='get_book')
]

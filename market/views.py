from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Book


def get_books(request):
    books = Book.objects.all()
    books_return = []
    for book in books:
        books_return.append({
            'name': book.name,
            'price': book.price,
            'page': book.page_count
        }

        )
    return JsonResponse(books_return, safe=False)


def get_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    books_return = {
        'name': book.name,
        'price': book.price,
        'page': book.page_count
    }
    return JsonResponse(books_return, safe=False)



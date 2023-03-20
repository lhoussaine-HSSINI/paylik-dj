from django.shortcuts import render

from . import models

def book_list(request):
    books = models.Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

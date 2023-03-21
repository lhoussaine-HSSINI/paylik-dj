from django.shortcuts import render
from django.http import Http404

from . import models

def book_list(request):
    books = models.Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def author_details(request, id) :
    try :
        author = models.Author.objects.get(pk=id) 
        return render(request, 'books/author_details.html', {'author': author})
    except models.Author.DoesNotExist as ex :
        raise Http404 

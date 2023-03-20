from django.shortcuts import render

def book_list(request):
    books = ['The Great Gatsby', 'To Kill a Mockingbird', '1984']
    return render(request, 'books/book_list.html', {'books': books})

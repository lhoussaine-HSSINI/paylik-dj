from books.models import Book, Author
from rest_framework.response import Response
from books.Serializer import BookSerializer, AuthorSerializer
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def book_list(request):
    try:
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        raise Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def author_details(request, id):
    try:
        author = Author.objects.get(pk=id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Author.DoesNotExist as ex:
        raise Response(status=status.HTTP_404_NOT_FOUND)

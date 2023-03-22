from rest_framework import serializers

from books.models import Book, Author

class SimpleBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'rating']

class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    books = SimpleBookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'description', 'score', 'books'] 


class BookSerializer(serializers.ModelSerializer):
    author = SimpleAuthorSerializer()
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'rating', 'author']

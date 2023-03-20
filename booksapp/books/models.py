from django.db import models


class Author (models.Model) :
    name = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return self.name

class Book (models.Model) :
    title = models.CharField(null=False, blank=False, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    added_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.title} by {self.author.name}'

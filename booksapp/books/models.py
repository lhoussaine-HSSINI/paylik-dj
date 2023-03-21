from django.db import models

from main.models import BaseModel
from main.utils import round_decimal
from .constants import *

# TODO Add signals to calculate stats like author's score, book's rating

class Author (BaseModel) :
    name = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=False, blank=False)

    @property
    def score(self) :
        books = self.book_set.all()
        ratings_sum = sum([book.rating for book in books])
        return round_decimal(ratings_sum / books.count(), 2)

    def __str__(self):
        return self.name


class Book (BaseModel) :
    title = models.CharField(null=False, blank=False, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    @property
    def rating (self) :
        reviews = self.review_set.all()
        reviews_sum = reviews.aggregate(models.Sum('review')).get('review__sum', 0)

        if reviews_sum == None : return 0

        return round_decimal(reviews_sum / reviews.count(), 2)

    def __str__(self):
        return f'{self.title} by {self.author}'


class Review (BaseModel) :
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.IntegerField(choices=REVIEWS_CHOICES)

    def __str__(self) :
        return f'{self.book} '

from django.db import models

from main.models import BaseModel
from main.utils import round_decimal
from .constants import *

class Author (BaseModel) :
    name = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=False, blank=False)
    score = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Book (BaseModel) :
    title = models.CharField(null=False, blank=False, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.title} by {self.author}'


class Review (BaseModel) :
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.IntegerField(choices=REVIEWS_CHOICES)

    def __str__(self) :
        return f'{self.book} '

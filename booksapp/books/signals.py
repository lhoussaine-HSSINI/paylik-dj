from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.db.models import Sum

from .models import Book, Review
from main.utils import round_decimal

def update_book_rating (book) :
    reviews = book.review_set.all()
    reviews_sum = reviews.aggregate(Sum('review')).get('review__sum', 0)

    if reviews_sum == None : return 0

    book.rating = round_decimal(reviews_sum / reviews.count(), 2)
    book.save()

def update_author_rating (author) :
    books = author.books.all()
    ratings_sum = sum([book.rating for book in books])

    author.score = round_decimal(ratings_sum / books.count(), 2)
    author.save()

# @receiver([post_save, post_delete], sender=Review)
def review_saved(sender, instance, **kwargs) :
    update_book_rating(instance.book)

# @receiver([post_save, post_delete], sender=Book)
def book_saved(sender, instance, **kwargs) :
    update_author_rating(instance.author)

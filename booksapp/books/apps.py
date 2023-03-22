from django.apps import AppConfig
from django.db.models.signals import post_delete, post_save


class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'

    def ready(self) :
        from .models import Book, Review
        from . import signals

        post_save.connect(signals.book_saved, sender=Book)
        post_delete.connect(signals.book_saved, sender=Book)
        post_save.connect(signals.review_saved, sender=Review)
        post_delete.connect(signals.review_saved, sender=Review)

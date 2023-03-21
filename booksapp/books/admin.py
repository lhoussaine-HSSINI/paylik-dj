from django.contrib import admin

from . import models

@admin.register(models.Book)
class BookAdmin (admin.ModelAdmin) :
    list_display = ('id', 'title', 'author', 'added_date', 'updated_date')
    ordering = ('id',)

@admin.register(models.Author)
class AuthorAdmin (admin.ModelAdmin) :
    list_display = ('id', 'name', 'added_date', 'updated_date')
    ordering = ('id',)


@admin.register(models.Review)
class ReviewAdmin (admin.ModelAdmin) :
    list_display = ('id', 'review', 'book', 'added_date', 'updated_date')
    ordering = ('id',)

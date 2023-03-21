from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('author/<int:id>', views.author_details, name='author_details'),
]

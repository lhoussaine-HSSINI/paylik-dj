from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.book_list),
    path('authors/<int:id>', views.author_details),
]

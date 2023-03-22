from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.book_list),
    path('author/<int:id>/', views.author_details),
]

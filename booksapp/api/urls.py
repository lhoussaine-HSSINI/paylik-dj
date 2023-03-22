from django.urls import path, include
# from  .views import book_list
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

rest_framework_router = routers.DefaultRouter()

urlpatterns = [
    path('', include(rest_framework_router.urls)),
    path('list_books/', views.book_list),
    path('author_details/<int:id>/', views.author_details),
]

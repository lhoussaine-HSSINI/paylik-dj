from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views

rest_framework_router = routers.DefaultRouter()

urlpatterns = [
    path('', include(rest_framework_router.urls)),
    path('auth/', include('api.auth.urls')),
    path('books/', views.book_list),
    path('author/<int:id>/', views.author_details),
]

from django.urls import path, include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

rest_framework_router = routers.DefaultRouter()

urlpatterns = [
    path('', include(rest_framework_router.urls)),
    path('auth/', include('api.auth.urls')),
    path('books/', include('api.books.urls')),
]

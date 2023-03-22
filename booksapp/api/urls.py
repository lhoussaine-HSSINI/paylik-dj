from django.urls import path, include

from rest_framework import routers

rest_framework_router = routers.DefaultRouter()

urlpatterns = [
    path('', include(rest_framework_router.urls)),
    path('auth/', include('api.auth.urls')),
]

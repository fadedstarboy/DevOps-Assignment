from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeeksModelViewSet

router = DefaultRouter()
router.register(r'users', GeeksModelViewSet, basename='users')
urlpatterns = [
    path('', include(router.urls)),
    
]
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
]

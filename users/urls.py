from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
]

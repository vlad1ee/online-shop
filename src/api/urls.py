from django.urls import path, include
from .views import UserDetail

urlpatterns = [
    path('user/<int:pk>/', UserDetail.as_view()),
]

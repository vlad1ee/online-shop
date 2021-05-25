from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import uuid_verify, sign_up, user_login, user_update


urlpatterns = [
    path('verify/<str:uuid>/', uuid_verify, name='verify'),
    path('sign-up/', sign_up, name='sign_up'),
    path('edit/<int:pk>/', user_update, name='edit'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

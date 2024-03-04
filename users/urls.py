from django.urls import path
from .views import UserRegistrationView, UserLoginView

urlpatters = [
  path('register/', UserRegistrationView.as_view()),
  path('login/', UserLoginView.as_view())
]

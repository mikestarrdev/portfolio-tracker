from django.urls import path
from .views import (
  UserRegistrationView,
  UserLoginView,
  UserLogoutView,
  ProtectedView
  )

urlpatterns = [
  path('register/', UserRegistrationView.as_view()),
  path('login/', UserLoginView.as_view()),
  path('logout/', UserLogoutView.as_view()),
  path('protected/', ProtectedView.as_view())
]

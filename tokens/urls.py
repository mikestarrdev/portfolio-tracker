from django.urls import path
from .views import TokenListCreateView, TokenDetailView

urlpatterns = [
    path('tokens/', TokenListCreateView.as_view()),
    path('tokens/<int:pk>/', TokenDetailView.as_view()),
]

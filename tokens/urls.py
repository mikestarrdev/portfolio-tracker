from django.urls import path
from .views import TokenListCreateView, TokenDetailView

urlpatterns = [
    path('tokens/', TokenListCreateView.as_view(), name='token-list-create'),
    path('tokens/<int:pk>/', TokenDetailView.as_view(), name='token-detail'),
]

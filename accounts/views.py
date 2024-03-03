# accounts/views.py
# pylint: disable=no-member

from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer

# this function can handle bulk GET and POST actions on all data (thanks to generics.ListCreateAPIView)
class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# this function can handle all CRUD actions, only on individual rows of data
class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

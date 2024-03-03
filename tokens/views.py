# pylint: disable=no-member

from rest_framework import generics
from .models import Token
from .serializers import TokenSerializer

class TokenListCreateView(generics.ListCreateAPIView):
    serializer_class = TokenSerializer

    def get_queryset(self):
        queryset = Token.objects.all()
        contract_address = self.request.query_params.get('contract_address', None)
        name = self.request.query_params.get('name', None)
        symbol = self.request.query_params.get('symbol', None)

        if contract_address:
            queryset = queryset.filter(contract_address=contract_address)
        if name:
            queryset = queryset.filter(name=name)
        if symbol:
            queryset = queryset.filter(symbol=symbol)

        return queryset

class TokenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

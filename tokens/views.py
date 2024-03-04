# pylint: disable=no-member

from rest_framework import generics
from .models import Token
from .serializers import TokenSerializer

class TokenListCreateView(generics.ListCreateAPIView):
    serializer_class = TokenSerializer

    def get_queryset(self):
        queryset = Token.objects.all()
        contract_address = self.request.query_params.get('contract_address', None)

        if contract_address:
            queryset = queryset.filter(contract_address=contract_address)

        return queryset

class TokenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

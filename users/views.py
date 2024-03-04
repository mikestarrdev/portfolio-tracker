from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.object.all()
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserProfileSerializer(user).data, status=status.HTTP_201_CREATED)

class UserLoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        # TODO: ADD LOGIN LOGIC BELOW
        # Add your login logic here
        # Authenticate the user, generate tokens, etc.
        return Response("Losin successful", status=status.HTTP_200_OK)

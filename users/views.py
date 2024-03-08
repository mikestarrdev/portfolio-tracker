from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserProfileSerializer(user).data, status=status.HTTP_201_CREATED)

class UserLoginView(LoginView):
    template_name = 'login.html'  # You can customize the login template if needed

class UserLogoutView(LogoutView):
    next_page = '/'  # Redirect to this URL after logout

class ProtectedView(LoginRequiredMixin, generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "This is a protected view for authenticated users."})

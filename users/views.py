from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer
from .models import Profile

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()

        return Response(ProfileSerializer(profile.profile).data, status=status.HTTP_201_CREATED)

class UserLoginView(LoginView):
    template_name = 'login.html'  # You can customize the login template if needed

class UserLogoutView(LogoutView):
    next_page = '/'  # Redirect to this URL after logout

class ProtectedView(LoginRequiredMixin, generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "This is a protected view for authenticated users."})

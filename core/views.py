from django.contrib.auth import get_user_model, login, logout
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from core.serializers import RegistrationSerializer, LoginSerializer, UpdatePasswordSerializer, UserSerializer

USER_MODEL = get_user_model()


class RegistrationView(generics.CreateAPIView):
    model = USER_MODEL
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(serializer.data)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePasswordView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def get_object(self):
        return self.request.user

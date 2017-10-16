from rest_framework.generics import (
        ListAPIView,
        CreateAPIView,
        RetrieveAPIView,
        RetrieveUpdateAPIView,
        DestroyAPIView,
    )

from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import renderers, generics
from rest_framework.permissions import IsAuthenticated

from accounts.models import Profile, User

from .serializers import (
        ProfileListSerializer,
        ProfileSerializer,
        UserListSerializer,
        UserSerializer,
    )

#=============== Profile API ===============

class ProfileListAPIView(ListAPIView):
    serializer_class = ProfileListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Profile.objects.all()
        return queryset_list

class ProfileDetailAPIView(RetrieveAPIView):
    serializer_class = ProfileListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Profile.objects.all()
        return queryset_list

class ProfileCreateAPIView(CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        post = super().post(request, *args, **kwargs)
        instance = Profile.objects.last()
        new_user = User()
        new_user.profile_id = instance.id
        new_user.save()
        return post

class ProfileUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()

class ProfileDeleteAPIView(DestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()

#=============== User API ===============

class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()
        return queryset_list

class UserDetailAPIView(RetrieveAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = User.objects.all()
        return queryset_list

class UserUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDeleteAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK

@api_view(["POST"])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = authenticate(email=email, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)
    return Response({"detail": "Logged in successfully"}, status=HTTP_200_OK)
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

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

class ProfileCreateAPIView(CreateAPIView):
    serializer_class = ProfileSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.filter(email=request.data['email'])
        if profile is not None:
            return Response({"detail": "Email exist", "status_code": 201})
        post = super().post(request, *args, **kwargs)
        instance = Profile.objects.last()
        new_user = User()
        new_user.profile_id = instance.id
        if 'nick_name' in request.data:
            new_user.nick_name = request.data['nick_name']
        new_user.save()
        return post

    def perform_create(self, serializer):
        hashed_password = make_password(serializer.validated_data['password']) # get the hashed password
        serializer.validated_data['password'] = hashed_password
        print(59, serializer.validated_data)
        user = super().perform_create(serializer)

class ProfileUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    # permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()

class ProfileDeleteAPIView(DestroyAPIView):
    serializer_class = ProfileSerializer
    # permission_classes = (IsAuthenticated,)
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
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDeleteAPIView(DestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, logout
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from django.contrib.auth.decorators import login_required

@api_view(['POST'])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = authenticate(email=email, password=password)
    if user is None:
        return Response({"detail": "Loged in error", "status_code": 400})
    profile = ProfileSerializer(user).data
    return Response({"detail": "Logged in successfully", "profile": profile, "status_code": 200}, status=HTTP_200_OK)
   
@api_view()
def logout(request):
    if request.user.is_authenticated:
        logout(request)
    return Response({"detail": "Logged out successfully", "status_code": 200})

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

class ProfileCreateAPIView(CreateAPIView):
    serializer_class = ProfileSerializer
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        print(45, request.data)
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
        user = super().perform_create(serializer)

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
    
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from django.contrib.auth.decorators import login_required

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def login(request):
    user_serializer = ProfileSerializer(request.user)
    profile_id = user_serializer.data['id']
    user =  User.objects.filter(profile_id=profile_id).first()
    profile = user_serializer.data
    if user is not None:
        profile['nick_name'] = user.nick_name
    return Response({"detail": "Logged in successfully", "profile": profile}, status=HTTP_200_OK)
   
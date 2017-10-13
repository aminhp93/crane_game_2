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

from accounts.models import Profile, User

from .serializers import (
		ProfileListSerializer,
		ProfileSerializer,
		UserListSerializer,
		UserSerializer,
	)

# Profile API

class ProfileListAPIView(ListAPIView):
	serializer_class = ProfileListSerializer

	def get_queryset(self, *args, **kwargs):
		queryset_list = Profile.objects.all()
		return queryset_list

class ProfileCreateAPIView(CreateAPIView):
	serializer_class = ProfileSerializer

class ProfileDetailAPIView(RetrieveAPIView):
	serializer_class = ProfileListSerializer

	def get_queryset(self, *args, **kwargs):
		queryset_list = Profile.objects.all()
		return queryset_list

class ProfileUpdateAPIView(RetrieveUpdateAPIView):
	serializer_class = ProfileSerializer
	queryset = Profile.objects.all()

class ProfileDeleteAPIView(DestroyAPIView):
	serializer_class = ProfileSerializer
	queryset = Profile.objects.all()


# User API

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

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserSerializer

class UserUpdateAPIView(RetrieveUpdateAPIView):
	serializer_class = UserSerializer
	queryset = User.objects.all()

class UserDeleteAPIView(DestroyAPIView):
	serializer_class = UserSerializer
	queryset = User.objects.all()
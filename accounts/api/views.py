from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import renderers, generics
from rest_framework.decorators import api_view

from accounts.models import Profile

from .serializers import (
        ProfileSerializer,
        ProfileUpdateSerializer
    )

from rest_framework.generics import CreateAPIView


#=============== Profile API ===============

class ProfileCreateAPIView(CreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


@api_view()
def profilelist_serializer(request):
    queryset = Profile.objects.all()
    serializers = ProfileSerializer(queryset, many=True)
    return Response({"status_code": 200, "msg": "success", "data": serializers.data})

@api_view()
def profiledetail_serializer(request, pk):
    queryset = Profile.objects.get(id=pk)
    serializers = ProfileSerializer(queryset)
    return Response({"status_code": 200, "msg": "success", "data": serializers.data})

@api_view(['POST'])
def profilecreate_serializer(request):
    if request.method == "POST":
        profile = Profile.objects.filter(email=request.data['email']).first()
        if profile is not None:
            return Response({"status_code": 201, "msg": "Email Exist"})
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status_code": 200, "msg": "Created successfully", "data": serializers.data})
        return Response({"status_code": 400, "msg": "Error"})

@api_view(['POST', 'GET'])
def profileupdate_serializer(request, pk):
    queryset = Profile.objects.get(id=pk)
    if request.method == "GET":
        serializers = ProfileUpdateSerializer(queryset)
        return Response({"status_code": 200, "msg": "success", "data": serializers.data})
    elif request.method == "POST":
        serializers = ProfileSerializer(queryset, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status_code": 200, "msg": "Updated successfully", "data": serializers.data})
        return Response({"status_code": 400, "msg": "Error"})

@api_view(['POST'])
def profiledelete_serializer(request, pk):
    if request.method == "POST":
        queryset = Profile.objects.get(id=pk)
        queryset.delete()
        return Response({"status_code": 400, "msg": "Delete successfully"})
    return Response({})

@api_view(['POST'])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    profile = Profile.objects.filter(email=email, password=password).first()
    if profile is None:
        return Response({"msg": "Loged in error", "status_code": 400})
    data = ProfileSerializer(profile).data
    return Response({"msg": "Logged in successfully", "data": data, "status_code": 200})

@api_view()
def logout(request):
    return Response({"msg": "Logged out successfully", "status_code": 200})

@api_view()
def search(request):
    email_params = request.query_params.get('q', None)
    if email_params is not None:
        profile = Profile.objects.filter(email=email_params).first()
        if profile is not None:
            profile_serializer = ProfileSerializer(profile)
            data = profile_serializer.data
            return Response({"status_code": 200, "msg": "Email Found", "data": data})
        return Response({"status_code": 400, "msg": "Email not found"})
    return Response({"status_code": 400, "msg": "Missing search params"})

@api_view(['POST'])
def check_email_exist(request):
    email = request.data.get('email',None)
    if email is not None:
        profile = Profile.objects.filter(email=email).first()
        if profile is not None:
            profile_serializer = ProfileSerializer(profile)
            data = profile_serializer.data
            return Response({"status_code": 200, "msg": "Email Found", "data": data})
        return Response({"status_code": 400, "msg": "Email not found"})
    return Response({"status_code": 400, "msg": "Email not provided"})

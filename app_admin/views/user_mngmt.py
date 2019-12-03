from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from app_admin.serializers import *

def login_page(request):
    return render(request,'login.html')

def signup_page(request):
    return render(request,'register.html')


class userCreate(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


# class userCreate(generics.CreateAPIView):
#     users = User.objects.all()
#     serializer_class = UserCreateSerializer
    
class UserLogin(APIView):
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data['username']
            user = User.objects.get(username=username)
            login(request, user)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=Http404)


class UserLogout(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, format=None):
        logout(request)
        return Response(template_name='login.html')
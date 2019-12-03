from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from django.contrib.auth.decorators import login_required
from app_employee.models import *
from app_employee.serializers import *


def tasks_list(request):
    return render(request,'tasks.html')


@login_required
def task_create(request):
    return render(request,'task-create.html')


def task_details(request, pk):
    return render(request,'task-details.html')


class taskListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        tasks = Task.objects.filter(is_active=True)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data, status=200)


class taskDetailsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk, is_active=True)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        task = TaskDetailSerializer(task)
        return Response(task.data)


class taskUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk, is_active=True)
        except Task.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskUpdateSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=404)


class taskDestroyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk, is_active=True)
        except Task.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        task = self.get_object(pk)
        task.is_active = False
        task.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class taskCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

# class taskDetailAPIView(generics.RetrieveAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class taskUpdateAPIView(generics.UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class taskDestroyAPIView(generics.DestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class taskCreateAPIView(generics.CreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
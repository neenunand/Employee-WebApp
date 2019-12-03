from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from app_employee.models import *
from app_employee.serializers import *


def employees_list(request):
    return render(request,'employees.html')


def employee_create(request):
    return render(request,'employee-create.html')


def employee_details(request, pk):
    return render(request,'employee-details.html')


class employeeListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        employees = Employee.objects.filter(is_active=True)
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data, status=200)


class employeeDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk, is_active=True)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        employee = EmployeeSerializer(employee)
        return Response(employee.data)


class employeeUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk, is_active=True)
        except Employee.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeUpdateSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=404)


class employeeDestroyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk, is_active=True)
        except Employee.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        employee = self.get_object(pk)
        employee.is_active = False
        employee.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class employeeCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = EmployeeCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


# class employeeListAPIView(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class employeeDetailAPIView(generics.RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class employeeUpdateAPIView(generics.UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeUpdateSerializer

# class employeeDestroyAPIView(generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class employeeCreateAPIView(generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class employeeList(APIView):
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees,many=True)
#         return Response(serializer.data, status=200)

#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=400)


# class employeeDetails(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         employee = EmployeeSerializer(employee)
#         return Response(employee.data)

#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=404)

#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


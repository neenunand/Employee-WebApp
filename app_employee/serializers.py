from rest_framework import serializers
from django.core.exceptions import ValidationError
from app_employee.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {"is_active":{"required":True}}

    def validate(self, data):
        emp_id = data['emp_id']
        employee_qs = Employee.objects.filter(emp_id=emp_id)
        if employee_qs.exists():
            raise ValidationError("This Employee Id already exists.")
        return data

    def create(self, validated_data):
        firstname = validated_data['firstname']
        lastname = validated_data['lastname']
        emp_id = validated_data['emp_id']
        employee = Employee(
            firstname = firstname,
            lastname = lastname,
            emp_id = emp_id,
        )
        employee.save()
        return validated_data


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','firstname','lastname']


class TaskListSerializer(serializers.ModelSerializer):
    assignee = serializers.CharField(source='assignee.firstname')

    class Meta:
        model = Task
        fields = ['id','taskname','assignee','start_date','end_date','status']


class TaskCreateSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(input_formats=["%d/%m/%Y"], required=True)
    end_date = serializers.DateTimeField(input_formats=["%d/%m/%Y"], required=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        taskname = validated_data['taskname']
        assignee = validated_data['assignee']
        start_date = validated_data['start_date']
        end_date = validated_data['end_date']
        status = validated_data['status']
        task = Task(
            taskname = taskname,
            assignee = assignee,
            start_date = start_date,
            end_date = end_date,
            status = status,
        )
        task.save()
        return validated_data


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskUpdateSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(input_formats=["%d/%m/%Y"], required=True)
    end_date = serializers.DateTimeField(input_formats=["%d/%m/%Y"], required=True)
    class Meta:
        model = Task
        fields = ['taskname','assignee','start_date','end_date','status']

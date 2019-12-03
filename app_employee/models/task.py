from django.db import models
from app_employee.models.employee import Employee

class Task(models.Model):
    assignee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
    taskname = models.TextField()
    status = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
from django.conf.urls import url, include

urlpatterns = [
    url('', include('app_employee.urls.employee_mngmt')),
    url('', include('app_employee.urls.task_mngmt')),
]
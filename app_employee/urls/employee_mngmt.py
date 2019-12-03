from django.conf.urls import url
from app_employee.views import employee_mngmt

urlpatterns = [
    url(r'^$', employee_mngmt.employees_list),
    url(r'^create$', employee_mngmt.employee_create),
    url(r'^details/(?P<pk>\d+)$', employee_mngmt.employee_details),
    url(r'^api/list$', employee_mngmt.employeeListAPIView.as_view()),
    url(r'^api/create$', employee_mngmt.employeeCreateAPIView.as_view()),
    url(r'^api/delete/(?P<pk>\d+)$', employee_mngmt.employeeDestroyAPIView.as_view()),
    url(r'^api/details/(?P<pk>\d+)$', employee_mngmt.employeeDetailAPIView.as_view()),
    url(r'^api/edit/(?P<pk>\d+)$', employee_mngmt.employeeUpdateAPIView.as_view()),
]
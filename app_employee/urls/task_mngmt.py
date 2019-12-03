from django.conf.urls import url
from app_employee.views import task_mngmt

urlpatterns = [
    url(r'^tasks$', task_mngmt.tasks_list),
    url(r'^task/create$', task_mngmt.task_create),
    url(r'^task/details/(?P<pk>\d+)$', task_mngmt.task_details),
    url(r'^api/tasks/list$', task_mngmt.taskListAPIView.as_view()),
    url(r'^api/task/create$', task_mngmt.taskCreateAPIView.as_view()),
    url(r'^api/task/delete/(?P<pk>\d+)$', task_mngmt.taskDestroyAPIView.as_view()),
    url(r'^api/task/details/(?P<pk>\d+)$', task_mngmt.taskDetailsAPIView.as_view()),
    url(r'^api/task/edit/(?P<pk>\d+)$', task_mngmt.taskUpdateAPIView.as_view()),
]
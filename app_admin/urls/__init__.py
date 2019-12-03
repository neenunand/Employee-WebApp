from django.conf.urls import url, include

urlpatterns = [
    url('', include('app_admin.urls.user_mngmt')),
]
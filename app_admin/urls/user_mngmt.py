from django.conf.urls import url
from app_admin.views import user_mngmt

urlpatterns = [
    url(r'^login/$', user_mngmt.login_page),
    url(r'^$', user_mngmt.login_page),
    url(r'^register$', user_mngmt.signup_page),
    url(r'^user/api/register$', user_mngmt.userCreate.as_view()),
    url(r'^user/api/login$', user_mngmt.UserLogin.as_view()),
    url(r'^user/api/logout$', user_mngmt.UserLogout.as_view()),
]
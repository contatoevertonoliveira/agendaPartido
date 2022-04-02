from django.urls import path
from login.views import *

urlpatterns = [
  path('', login_user),
  path('submit', submit_login),
  path('logout', logout_user),
]
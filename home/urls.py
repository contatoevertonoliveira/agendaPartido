from django.urls import path
from home.views import *

urlpatterns = [
  path('', homeView, name='homeView'),
  path('submit', homeSubmit, name='createMember'),
  path('lista/', listMembers, name='listMember'),
  path('update/<int:id>/', updateMember, name='updateMember'),
  path('delete/<int:id>/', deleteMember, name='deleteMember'),
]
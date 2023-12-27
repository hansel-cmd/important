from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('auth/', obtain_auth_token)
]

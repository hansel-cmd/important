from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('sign-up', views.sign_up, name = 'sign_up'),
    path('complete', views.complete, name = 'complete'),
    path('details', views.details, name = 'details'),
    path('order', views.place_order, name = 'order'),
]

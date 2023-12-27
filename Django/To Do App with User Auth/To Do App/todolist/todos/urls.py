from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('all/', views.index, name = 'index'),
    path('pending/', views.pending, name = 'pending'),
    path('completed/', views.completed, name = 'completed'),
    path('update/', views.update_completed, name = 'update_completed'),
    path('delete/', views.delete, name = 'delete'),
    path('add/', views.add, name = 'add'),
    path('test/', views.MyTestView.as_view(), name = 'test'),
    path('logout/', views.log_out, name = 'logout'),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
]

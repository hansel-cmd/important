from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('logout/', views.log_out, name = 'logout'),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('signup/', views.SignupView.as_view(), name = 'signup'),
    path('blog-details/<int:id>', views.blog_details, name = 'blog-details'),
    path('create/', views.CreateView.as_view(), name = 'create'),
    path('favorites/', views.favorites, name = 'favorites'),
    path('favorites/<int:id>', views.add_favorites, name = 'add_favorites'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('update/<int:id>', views.UpdateView.as_view(), name = 'update'),
]

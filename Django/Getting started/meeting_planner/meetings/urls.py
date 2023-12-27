from django.urls import path
from . import views

app_name = 'meetings'

urlpatterns = [
    path('meeting_planner/detail/<int:id>', views.detail, name = 'detail'),
    path('meeting_planner/rooms', views.rooms_list, name = 'rooms'),
    path('meeting_planner/new', views.new, name = 'new'),
]

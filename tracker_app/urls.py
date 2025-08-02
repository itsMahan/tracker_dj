from django.urls import path
from . import views




urlpatterns = [
    path('list', views.list_trackers, name='list_trackers'),
    path('add', views.add_tracker, name='add_tracker'),
    path('delete/<int:id>', views.delete_tracker, name='delete_tracker'),
]
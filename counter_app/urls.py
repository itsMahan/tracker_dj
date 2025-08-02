from django.urls import path
from . import views


urlpatterns = [
    path('list', views.list_counters),
    path('add', views.add_counter),
    path('delete/<int:id>', views.delete_counter, name='delete_counter'),
]
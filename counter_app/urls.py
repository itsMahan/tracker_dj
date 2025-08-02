from django.urls import path
from . import views


urlpatterns = [
    path('list', views.list_counters, name='list_counters'),
    path('add', views.add_counter, name='add_counter'),
    path('delete/<int:id>', views.delete_counter, name='delete_counter'),
    path('reset/<int:id>', views.reset_counter, name='reset_counter'),
]
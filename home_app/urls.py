from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.show_all, name='show_all'),
]
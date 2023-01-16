from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('all_employ', views.all_employ, name='all_employ'),
    path('add_employ', views.add_employ, name='add_employ'),
    path('remove_employ', views.remove_employ, name='remove_employ'),
    path('remove_employ/<int:emp_id>', views.remove_employ, name='remove_employ'),
    path('filter_employ', views.filter_employ, name='filter_employ'),
]
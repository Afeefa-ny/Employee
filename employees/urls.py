from django.urls import path
from . import views
urlpatterns = [
    path('', views.employee_list, name='list'),
    path('add/', views.add_employee, name='add'),
    path('employee/<int:id>/', views.employee_detail, name='detail'),
    path('delete/<int:id>/', views.delete_employee, name='delete'),
    path('update/<int:id>/', views.update_employee, name='update'),
    path('api/employees/', views.api_employees),
]
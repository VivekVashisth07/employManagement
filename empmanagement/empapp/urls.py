from empapp.views import Employee
from django.urls import path

urlpatterns = [
    path('employ/', Employee.as_view()),
    path('employ/edit/', Employee.view_one),
    path('employ/update/', Employee.employ_update),
    path('employ/delete/', Employee.delete_one),
]

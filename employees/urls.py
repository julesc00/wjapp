from django.urls import path

from employees.views import list_employees

app_name = "employees"

urlpatterns = [
    path("", list_employees, name="list-employees")
]

from django.shortcuts import render, reverse
from .models import Department
from .forms import DepartmentModelForm
from django.views.generic import ListView, CreateView

class DepartmentListView(ListView):
    template_name = 'department/department_list.html'
    context_object_name = "departments"

    def get_queryset(self):
        queryset = Department.objects.all()
        return queryset


class DepartmentCreateView(CreateView):
    template_name = "department/department_create.html"
    form_class = DepartmentModelForm

    def get_success_url(self):
        return reverse('departments:department-list-view')

from django.shortcuts import render, reverse
from .models import Department
from .forms import DepartmentModelForm
from django.views.generic import ListView, CreateView, DetailView

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


from teacher.models import Teacher
from course.models import Course

class DepartmentDetailView(DetailView):

    template_name = 'department/department_detail.html'
    context_object_name = "department"

    def get_queryset(self):
        queryset = Department.objects.all()
        return queryset


    def get_context_data(self, *args, **kwargs):
        context = super(DepartmentDetailView, self).get_context_data(*args, **kwargs)

        teachers = Teacher.objects.filter(deptt__id = self.object.id)
        courses = Course.objects.filter(department__id = self.object.id)

        context['teachers'] = teachers
        context['courses'] = courses

        return context
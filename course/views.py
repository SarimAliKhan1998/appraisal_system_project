from django.shortcuts import render, reverse
from .models import Course
from .forms import CourseModelForm
from django.views.generic import ListView, CreateView

class CourseListView(ListView):
    template_name = 'course/course_list.html'
    context_object_name = "courses"

    def get_queryset(self):
        queryset = Course.objects.all().order_by('department')
        return queryset


class CourseCreateView(CreateView):
    template_name = "course/course_create.html"
    form_class = CourseModelForm

    def get_success_url(self):
        return reverse('courses:course-list-view')

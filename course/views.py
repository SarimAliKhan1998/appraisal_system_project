from django.shortcuts import render, reverse
from .models import Course
from .forms import CourseModelForm
from django.views.generic import ListView, CreateView, DetailView

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



from .models import CourseClass
from .forms import CourseClassModelForm


class CourseClassListView(ListView):

    template_name = 'course_class/course_class_list.html'
    context_object_name = 'classes'

    def get_queryset(self):
        queryset = CourseClass.objects.all()
        return queryset



class CourseClassCreateView(CreateView):

    template_name = "course_class/course_class_create.html"
    form_class = CourseClassModelForm

    def get_success_url(self):
        return reverse('landing-page')


class CourseClassDetailView(DetailView):

    template_name = 'course_class/course_class_detail.html'
    context_object_name = 'class'

    def get_queryset(self):
        queryset = CourseClass.objects.all().order_by('course__department')
        return queryset
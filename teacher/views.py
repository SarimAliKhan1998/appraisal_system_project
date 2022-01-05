from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Teacher
from .forms import TeacherModelForm
import random


class TeacherListView(ListView):

    template_name = "teacher/teacher_list.html"
    context_object_name = 'teachers'
    
    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset



class TeacherCreateView(CreateView):

    template_name = 'teacher/teacher_create.html'
    form_class = TeacherModelForm

    def get_success_url(self):
        return reverse("landing-page")


    def form_valid(self, form):

        teacher = form.save(commit = False)
        teacher.is_admin = False
        teacher.is_teacher = True
        teacher.username = teacher.first_name + "_" + teacher.last_name + "_" + teacher.phone_no
        initial_password = random.randint(1, 100000)
        teacher.set_password(f"{initial_password}")

        department = form.cleaned_data.get('department')
        teacher.save()

        Teacher.objects.create(
            user = teacher,
            department = department,
            employee_id = 1212
        )

        return super(TeacherCreateView, self).form_valid(form)
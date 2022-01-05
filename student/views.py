from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Student
from .forms import StudentModelForm
import random


class StudentListView(ListView):

    template_name = "student/student_list.html"
    context_object_name = 'students'
    
    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset



class StudentCreateView(CreateView):

    template_name = 'student/student_create.html'
    form_class = StudentModelForm

    def get_success_url(self):
        return reverse("landing-page")


    def form_valid(self, form):

        student = form.save(commit = False)
        student.is_admin = False
        student.is_student = True
        student.username = student.first_name + "_" + student.last_name + "_" + student.phone_no
        initial_password = random.randint(1, 100000)
        student.set_password(f"{initial_password}")

        # dob = student.pop('date_of_birth')
        # department = student.pop('department')
        dob = form.cleaned_data.get('date_of_birth')
        department = form.cleaned_data.get('department')
        student.save()

        Student.objects.create(
            user = student,
            date_of_birth = dob,
            department = department,
            roll_no = 1212
        )

        return super(StudentCreateView, self).form_valid(form)
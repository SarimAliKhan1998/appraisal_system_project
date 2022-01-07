from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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


from course.models import CourseClass

class TeacherDetailView(DetailView):

    template_name = 'teacher/teacher_detail.html'
    context_object_name = 'teacher'

    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset

    
    def get_context_data(self, *args, **kwargs):
        context = super(TeacherDetailView, self).get_context_data(*args, **kwargs)

        teacher_classes = CourseClass.objects.filter(teacher__id = self.object.id).order_by('course')
        context['classes'] = teacher_classes

        return context


class TeacherUpdateView(UpdateView):

    template_name = "teacher/teacher_update.html"
    form_class = TeacherModelForm

    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('teachers:teacher-detail-view', args = (self.object.id,))

    # def get_form_kwargs(self):
    #     kwargs = super(TeacherUpdateView, self).get_form_kwargs()
    #     kwargs['request'] = self.request
    #     return kwargs

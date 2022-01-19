from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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



from course.models import CourseClass, Attendance

class StudentDetailView(DetailView):

    template_name = 'student/student_detail.html'
    context_object_name = 'student'

    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset

    
    def get_context_data(self, *args, **kwargs):
        context = super(StudentDetailView, self).get_context_data(*args, **kwargs)

        student_classes = CourseClass.objects.filter(students__id = self.object.id).order_by('course').all()
        context['classes'] = student_classes

        classes_dict = student_classes.values()
        print(classes_dict)

        for cls in classes_dict:
            attendance = Attendance.objects.filter(subject = cls['id']).filter(student = self.object.id)
            print(attendance)
            atten_received = 0
            total_atten = 0
            for entry in attendance:
                atten_received += entry.no_of_attendances_granted
                total_atten += entry.no_of_attendances_possible

            cls['attendance_received'] = atten_received
            cls['total_attendance'] = total_atten

            try:
                atten_percentage = round((atten_received/total_atten)*100, 2)
            except Exception as e:
                atten_percentage = 0

            cls['attendance_percentage'] = atten_percentage

            if atten_percentage >= 60:
                cls['eligibility'] = "Eligible"
            else:
                cls['eligibility'] = "Not Eligible"


        context['classes_dict'] = classes_dict

        return context



class StudentUpdateView(UpdateView):

    template_name = "students/student_update.html"
    form_class = StudentModelForm

    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('students:student-detail-view', args = (self.object.id,))


from django.shortcuts import render, reverse
from django.views.generic.edit import DeleteView
from .models import Course
from .forms import CourseModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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


from teacher.models import Teacher 

class CourseDetailView(DetailView):

    template_name = 'course/course_detail.html'
    context_object_name = 'course'

    def get_queryset(self):
        queryset = Course.objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(CourseDetailView, self).get_context_data(*args, **kwargs)

        # we get all the classes that are held for this particular course, from there we can extract all the teachers that are taking this course
        classes = CourseClass.objects.filter(course__id = self.object.id)
        context['classes'] = classes

        return context



class CourseUpdateView(UpdateView):

    template_name = "course/course_update.html"
    form_class = CourseModelForm

    def get_queryset(self):
        queryset = Course.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('course:course-detail-view', args = (self.object.id,))


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



class CourseClassUpdateView(UpdateView):

    template_name = "course_class/course_class_update.html"
    form_class = CourseClassModelForm

    def get_queryset(self):
        queryset = CourseClass.objects.all()
        return queryset

    def get_success_url(self):
        return reverse('course:course-class-detail-view', args = (self.object.id,))



from .models import Attendance
from django.db.models import Sum

def attendance_see_view(request, pk):

    context = {}
    print(pk)
    course_class = CourseClass.objects.get(id = pk)
    # course = Course.objects.get(id = pk)
    # print(course_class.course)
    # print(course_class.students.all())

    context['class'] = course_class

    attendance_records = Attendance.objects.filter(subject = pk)
    print(attendance_records)

    total_attendance = Attendance.objects.aggregate(Sum('no_of_attendances_possible'))
    print(total_attendance)


    # print(course)

    return render (request,'attendance/attendance_see_view.html',context)



from .forms import AttendanceGrantForm

def attendance_grant_view(request, pk):

    context = {}

    course_class = CourseClass.objects.get(id = pk)

    context['class'] = course_class

    context['form'] = AttendanceGrantForm



    return render(request, 'attendance/attendance_grant_view.html', context)
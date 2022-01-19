from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import User

def landing_page_view(request):

    return render(request, "landing_page.html", {})


class UserListView(ListView):
    template_name = "user/user_list.html"
    context_object_name = "users"

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


from teacher.models import Teacher
from student.models import Student


def login_redirect_view(request):

    if request.user.is_teacher:
        teacher = Teacher.objects.get(user__id = request.user.id)
        return redirect('teachers:teacher-detail-view', pk = (teacher.id))
    elif request.user.is_student:
        student = Student.objects.get(user__id = request.user.id)
        return redirect('students:student-detail-view', pk = (student.id))
    else:
        return render(request, "landing_page.html", {})


    # return render()

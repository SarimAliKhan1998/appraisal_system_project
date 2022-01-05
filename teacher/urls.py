from django.urls import path
from .views import TeacherListView, TeacherCreateView

app_name = "teachers"

urlpatterns = [
    path("", TeacherListView.as_view(), name = 'teacher-list-view'),
    path("create/", TeacherCreateView.as_view(), name = 'teacher-create-view'),
]

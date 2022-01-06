from django.urls import path
from .views import TeacherListView, TeacherCreateView, TeacherDetailView

app_name = "teachers"

urlpatterns = [
    path("", TeacherListView.as_view(), name = 'teacher-list-view'),
    path("create/", TeacherCreateView.as_view(), name = 'teacher-create-view'),
    path("<int:pk>/", TeacherDetailView.as_view(), name = 'teacher-detail-view'),
]

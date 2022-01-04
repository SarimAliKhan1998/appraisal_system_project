from django.urls import path
from .views import CourseListView, CourseCreateView

app_name = "courses"

urlpatterns = [
    path("", CourseListView.as_view(), name = 'course-list-view'),
    path('create/', CourseCreateView.as_view(), name = "course-create-view")
]

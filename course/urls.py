from django.urls import path
from .views import CourseListView, CourseCreateView
from .views import CourseClassListView, CourseClassCreateView, CourseClassDetailView

app_name = "courses"

urlpatterns = [
    path("", CourseListView.as_view(), name = 'course-list-view'),
    path('create/', CourseCreateView.as_view(), name = "course-create-view"),

    path('classes/create/', CourseClassCreateView.as_view(), name = 'course-class-create-view'),
    path('classes/', CourseClassListView.as_view(), name = 'course-class-list-view'),
    path('classes/<int:pk>', CourseClassDetailView.as_view(), name = 'course-class-detail-view'),
]

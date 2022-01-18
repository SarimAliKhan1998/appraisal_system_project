from django.urls import path
from .views import CourseListView, CourseCreateView, CourseDetailView, CourseUpdateView
from .views import CourseClassListView, CourseClassCreateView, CourseClassDetailView, CourseClassUpdateView
from .views import attendance_see_view, attendance_grant_view

app_name = "courses"

urlpatterns = [
    path("", CourseListView.as_view(), name = 'course-list-view'),
    path('create/', CourseCreateView.as_view(), name = "course-create-view"),
    path('<int:pk>/', CourseDetailView.as_view(), name = "course-detail-view"),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name = "course-update-view"),

    path('classes/create/', CourseClassCreateView.as_view(), name = 'course-class-create-view'),
    path('classes/', CourseClassListView.as_view(), name = 'course-class-list-view'),
    path('classes/<int:pk>/', CourseClassDetailView.as_view(), name = 'course-class-detail-view'),
    path('classes/<int:pk>/update/', CourseClassUpdateView.as_view(), name = 'course-class-update-view'),

    path('classes/attendance/<int:pk>/', attendance_see_view, name= 'attendance-see-view'),
    path('classes/attendance/<int:pk>/grant/', attendance_grant_view, name= 'attendance-grant-view')
]

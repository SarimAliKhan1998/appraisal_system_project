from django.urls import path
from .views import StudentListView, StudentCreateView, StudentDetailView

app_name = "students"

urlpatterns = [
    path("", StudentListView.as_view(), name = 'student-list-view'),
    path("create/", StudentCreateView.as_view(), name = 'student-create-view'),
    path("<int:pk>/", StudentDetailView.as_view(), name = 'student-detail-view'),
]

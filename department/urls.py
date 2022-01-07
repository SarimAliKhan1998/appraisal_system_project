from django.urls import path
from .views import DepartmentListView, DepartmentCreateView, DepartmentDetailView

app_name = "departments"

urlpatterns = [
    path("", DepartmentListView.as_view(), name = 'department-list-view'),
    path('create/', DepartmentCreateView.as_view(), name = "department-create-view"),
    path('<int:pk>/', DepartmentDetailView.as_view(), name = "department-detail-view"),
]

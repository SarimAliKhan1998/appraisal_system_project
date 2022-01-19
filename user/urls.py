from django.urls import path
from .views import UserListView, login_redirect_view

app_name = "users"

urlpatterns = [
    path("", UserListView.as_view(), name = 'user-list-view'),
    path("redirect/", login_redirect_view, name = 'login-redirect-view'),
]

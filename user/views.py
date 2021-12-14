from django.shortcuts import render
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



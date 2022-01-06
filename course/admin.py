from django.contrib import admin
from .models import Course
from .models import CourseClass

admin.site.register(Course)
admin.site.register(CourseClass)
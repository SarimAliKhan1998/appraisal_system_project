from django.contrib import admin
from .models import Course
from .models import CourseClass
from .models import Attendance

admin.site.register(Course)
admin.site.register(CourseClass)
admin.site.register(Attendance)
from django.db import models

class Course(models.Model):

    course_name = models.CharField(max_length=70)
    department = models.ForeignKey('department.Department', on_delete = models.CASCADE)

    def __str__(self):
        return self.name + f" - {self.department.department_name} Department"
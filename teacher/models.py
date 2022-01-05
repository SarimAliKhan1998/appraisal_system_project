from django.db import models
from user.models import User
from department.models import Department

class Teacher(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, blank = True, null=True)
    department = models.ForeignKey('department.Department', null = True, blank= True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user + " " + self.department